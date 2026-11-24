"""HTTP helpers shared by the clients."""
from typing import Optional, Union

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from .errors import CarmenAPIConfigError, CarmenAPIError
from .models import CloudServiceRegion

_REGION_URLS = {
    "AUTO": "https://api.carmencloud.com",  # latency-based routing
    "EU": "https://eu-central-1.api.carmencloud.com",
    "US": "https://us-east-1.api.carmencloud.com",
}


def select_api_base_url(
    endpoint: Optional[str],
    cloud_service_region: Optional[Union[CloudServiceRegion, str]],
) -> str:
    """Resolves the API base URL; `endpoint` wins over `cloud_service_region`."""
    if endpoint:
        return endpoint.rstrip("/")
    region = cloud_service_region.value if isinstance(cloud_service_region, CloudServiceRegion) else cloud_service_region
    url = _REGION_URLS.get(region or "AUTO")
    if url is None:
        raise CarmenAPIConfigError(f"Invalid 'cloud_service_region': '{cloud_service_region}'.")
    return url


def create_session(retry_count: Optional[int], retry_post: bool = False) -> requests.Session:
    """A session retrying throttled and failed requests with exponential backoff."""
    methods = ["HEAD", "GET", "OPTIONS", "PUT", "DELETE"]
    if retry_post:
        methods.append("POST")
    retry = Retry(
        total=3 if retry_count is None else retry_count,
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=methods,
        backoff_factor=1,
        raise_on_status=False,
    )
    session = requests.Session()
    session.mount("https://", HTTPAdapter(max_retries=retry))
    session.mount("http://", HTTPAdapter(max_retries=retry))
    return session


def raise_for_status(response: requests.Response) -> None:
    """Raises CarmenAPIError for a non-2xx response, with the API's error message."""
    if response.ok:
        return
    body = None
    message = f"HTTP {response.status_code}"
    try:
        body = response.json()
    except ValueError:
        body = response.text or None
    if isinstance(body, dict):
        message = body.get("message") or body.get("error_description") or body.get("error") or message
    raise CarmenAPIError(str(message), status=response.status_code, body=body)
