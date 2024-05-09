from dataclasses import dataclass
from typing import Optional, Tuple
from enum import Enum

from carmen_cloud_client.models import SortOrder
from ..errors import CarmenAPIConfigError

class CloudServiceRegion(Enum):
    """
    The cloud service region to use for the request.
    """
    AUTO = "AUTO"
    EU = "EU"
    US = "US"


@dataclass(frozen=True)
class StorageAndHookAPIOptions:
    """
    An object containing configuration options for the Storage & Hook API client.

    Attributes
    ----------
    api_key : str
        The API key to be used for authentication.
    endpoint : Optional[str]
        The URL of the API endpoint to call. Optional if `cloud_service_region`
        is also set. Overrides `cloud_service_region` if both properties are set.
    cloud_service_region : Optional[CloudServiceRegion]
        The cloud service region to use - `"EU"` for Europe and `"US"` for the
        United States. Has no effect if `endpoint` is also set.
    input_image_location : InputImageLocation
        The expected geographic region of the license plates in the uploaded image.
        You can either use one of the presets in the `Locations` object or provide
        your own settings in an `InputImageLocation(region="", location="")` object.
        `region` is required but `location` is optional.
    region_of_interest : Optional[RegionOfInterest]
        The region of interest in the image to be analyzed.
    services : SelectedServices
        The services to use. At least one of `anpr` (Automated Number Plate
        Recognition), `mmr` (Make and Model Recognition) and `adr` (Dangerous Goods
        Pictogram Recognition) must be specified.
    disable_call_statistics : Optional[bool] = False
        The service uses your call statistics, which were generated based on the
        list of locations (countries and states) determined when reading your
        previously sent images, to decide which ANPR engines should be run when
        processing your uploaded images. If you want the service to ignore your call
        statistics, for example because you use the service with images from
        different locations around the world, you can turn this feature off by
        setting the property value to `true`.
    disable_image_resizing : Optional[bool] = False
        The service resizes large images to Full HD resolution by bicubic
        interpolation. Resizing can make reading many times faster, but it can reduce
        the recognition efficiency. If you don't want the service to resize your
        images, turn this feature on by setting the property value to `true`. By
        disabling image resizing, you may also need to enable wide range analysis.
    enable_wide_range_analysis : Optional[bool] = False
        If you cannot guarantee that the uploaded image meets all the required
        parameters (see the Input Images tab on the How To Use page), you can turn
        on the wide-range analysis by setting this property's value to `true`.
        Attention! The duration of the analysis may increase several times.
    enable_unidentified_license_plate : Optional[bool] = False
        If you want to receive text results read from unidentified license plate
        types as well, you can turn this feature on by setting the property value to
        true. Attention! The number of false positives can be much higher.
    max_reads : Optional[int] = 1
        An optional parameter, it specifies the maximum number of vehicle/license
        plate searches per image. Use this parameter carefully, because every
        search increases the processing time. The system will stop searching when
        there is no more vehicle/license plate in the image, or the number of
        searches reaches the value of `max_reads`. Its value is `1` by default,
        the maximum is `5`.
    retry_count : Optional[int] = 3
        How many times the request should be retried in case of a 5XX response
        status code. Default: 3.
    """
    api_key: str
    endpoint: Optional[str] = None
    cloud_service_region: Optional[CloudServiceRegion] = None
    retry_count: Optional[int] = 3


class APIName(Enum):
    """
    The name of the API to get the events of.
    """
    Vehicle = "vehicle"
    TransportationAndCargo = "transport"


@dataclass(frozen=True)
class EventFilters:
    """
    Contains options for filtering recognition events.

    Attributes
    ----------

    limit: Optional[int] = 200
        The maximum number of events to return. Default: 200.
    order: Optional[SortOrder] = SortOrder.ASC
        The order in which to return events. Default: `"asc"`.
    continuation_token: Optional[str] = None
        The token to continue a previous request. If provided, the request will return
        events after the last event of the previous request.
    before: Optional[int] = 0
        The timestamp of the event to start at. If provided, the request will return
        events after or at the provided timestamp.

        **NOTE:** `before` and `after` are mutually exclusive.
    after: Optional[int] = 0
        The timestamp of the event to end at. If provided, the request will return
        events before or at the provided timestamp.

        **NOTE:** `before` and `after` are mutually exclusive.
    """
    limit: Optional[int] = 200
    order: Optional[SortOrder] = SortOrder.ASC
    continuation_token: Optional[str] = None
    before: Optional[int] = 0
    after: Optional[int] = 0
