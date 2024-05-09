import os
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from typing import List, Union
from requests.exceptions import RetryError
from urllib.parse import urljoin, urlencode
from carmen_cloud_client.errors import CarmenAPIConfigError, CarmenAPIError
from carmen_cloud_client.storage_and_hook.events_response import EventsResponse
from .options import APIName, EventFilters, StorageAndHookAPIOptions
from ..models import CloudServiceRegion

class StorageAndHookAPIClient:
    """
    A client for interacting with the Carmen Cloud Storage & Hook API.
    """

    def __init__(self, options: StorageAndHookAPIOptions) -> None:
        self.options = options
        self.api_url = self.get_parametrized_api_url()
        self.session = requests.Session()

        retry_strategy = Retry(
            total=3,
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=["HEAD", "GET", "OPTIONS", "POST"],
            backoff_factor=1
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("https://", adapter)

    def get_events(self, api: APIName, filters: EventFilters) -> EventsResponse:
        query_params = {
            'limit': filters.limit,
            'order': filters.order.value if filters.order else None,  # Assuming SortOrder is an Enum
            'continuation-token': filters.continuation_token,
            'before': filters.before,
            'after': filters.after
        }
        query_params = {k: v for k, v in query_params.items() if v is not None}

        base_url = urljoin(self.api_url, f'/events/{api}')
        url = f"{base_url}?{urlencode(query_params)}"

        response = None
        try:
            response = self.session.get(url)
            response.raise_for_status()
        except RetryError as e:
            raise CarmenAPIError(f"Failed to send request after {self.options.retry_count} retries: {e}")

        return EventsResponse.parse_obj(response.json())

    def select_api_base_url(self) -> str:
        if self.options.endpoint:
            return self.options.endpoint
        if self.options.cloud_service_region == "EU" or self.options.cloud_service_region == CloudServiceRegion.EU:
            return "https://eu-central-1.api.carmencloud.com"
        if self.options.cloud_service_region == "US" or self.options.cloud_service_region == CloudServiceRegion.US:
            return "https://us-east-1.api.carmencloud.com"
        if self.options.cloud_service_region == "AUTO" or self.options.cloud_service_region == CloudServiceRegion.AUTO or self.options.cloud_service_region is None:
            return "https://api.carmencloud.com" # latency-based routing
        raise CarmenAPIConfigError(f"Invalid 'cloud_service_region': '{self.options.cloud_service_region}'.")

    def get_parametrized_api_url(self) -> str:
        base_url = self.select_api_base_url()
        return urljoin(base_url, f"/storage")
