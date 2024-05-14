from dataclasses import dataclass
from typing import Optional, Tuple
from enum import Enum

from carmen_cloud_client.models import SortOrder
from ..errors import CarmenAPIConfigError
from ..models import CloudServiceRegion


@dataclass(frozen=True)
class DescriptorAPIOptions:
    """
    An object containing configuration options for the Descriptor API client.

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
    retry_count : Optional[int] = 3
        How many times the request should be retried in case of a 5XX response
        status code. Default: 3.
    """
    api_key: str
    endpoint: Optional[str] = None
    cloud_service_region: Optional[CloudServiceRegion] = None
    retry_count: Optional[int] = 3
