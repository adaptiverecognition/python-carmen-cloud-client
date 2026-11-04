import os
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder
from typing import List, Union
from io import BytesIO
from requests.exceptions import RetryError
from urllib.parse import urljoin
from carmen_cloud_client._http import create_session, raise_for_status, select_api_base_url
from carmen_cloud_client.errors import CarmenAPIConfigError, CarmenAPIError, InvalidImageError
from .options import VehicleAPIOptions, CloudServiceRegion
from .response import VehicleApiResponse

class VehicleAPIClient:
    supported_api_version: str = "1.4.1"

    def __init__(self, options: VehicleAPIOptions):
        self.options = options
        self.api_url = self.get_parametrized_api_url()

    def send(self, image_data_or_path: Union[str, bytes, BytesIO]) -> VehicleApiResponse:
        form_data = self.create_form_data(image_data_or_path)
        headers = self.create_headers(form_data.content_type)

        session = create_session(self.options.retry_count, retry_post=True)

        response = None
        try:
            response = session.post(self.api_url, headers=headers, data=form_data)
            raise_for_status(response)
        except RetryError as e:
            raise CarmenAPIError(f"Failed to send request after {self.options.retry_count} retries: {e}")

        return VehicleApiResponse.model_validate(response.json())

    def get_image_bytes(self, image_data_or_path: Union[str, bytes, BytesIO]) -> Union[bytes, BytesIO]:
        if isinstance(image_data_or_path, bytes) or isinstance(image_data_or_path, BytesIO):
            return image_data_or_path
        elif isinstance(image_data_or_path, str) and os.path.exists(image_data_or_path):
            with open(image_data_or_path, "rb") as f:
                return BytesIO(f.read())
        else:
            raise InvalidImageError(f"Argument must be either a valid file path, BytesIO or bytes, but was: '{image_data_or_path}'.")

    def create_headers(self, content_type) -> dict:
        headers = {
            "Content-Type": content_type,
            "X-Api-Key": self.options.api_key,
        }
        if self.options.disable_call_statistics:
            headers["x-disable-call-statistics"] = "true"
        if self.options.disable_image_resizing:
            headers["x-disable-image-resizing"] = "true"
        if self.options.enable_wide_range_analysis:
            headers["x-enable-wide-range-analysis"] = "true"
        if self.options.enable_unidentified_license_plate:
            headers["x-enable-unidentified-license-plate"] = "true"

        return headers

    def create_form_data(self, image_data_or_path: Union[str, bytes, BytesIO]) -> MultipartEncoder:
        fields = []
        image_bytes = self.get_image_bytes(image_data_or_path)
        fields.append(("service", self.create_service_parameter()))

        if self.options.input_image_location.location:
            fields.append(("location", self.options.input_image_location.location))

        if self.options.max_reads:
            fields.append(("maxreads", str(self.options.max_reads)))

        if self.options.region_of_interest:
            coords = [
                self.options.region_of_interest.top_left,
                self.options.region_of_interest.top_right,
                self.options.region_of_interest.bottom_right,
                self.options.region_of_interest.bottom_left,
            ]
            roi = ";".join([",".join(map(str, coord)) for coord in coords])
            fields.append(("roi", roi))

        fields.append(("image", ("image.jpg", image_bytes, "image/jpeg")))

        return MultipartEncoder(fields=fields)

    def create_service_parameter(self) -> str:
        services = []
        if self.options.services.anpr:
            services.append("anpr")
        if self.options.services.mmr:
            services.append("mmr")
        if self.options.services.adr:
            services.append("adr")
        if len(services) == 0:
            raise CarmenAPIConfigError(
                "At least one service (`anpr`, `mmr` or `adr`) must be specified."
            )
        return ",".join(services)

    def get_parametrized_api_url(self) -> str:
        base_url = select_api_base_url(self.options.endpoint, self.options.cloud_service_region)
        return urljoin(base_url, f"/vehicle/{self.options.input_image_location.region}")
