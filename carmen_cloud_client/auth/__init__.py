"""API key -> bearer access token exchange (``POST /auth/token``)."""
import threading
import time
from dataclasses import dataclass
from typing import Optional, Union

from .._http import create_session, raise_for_status, select_api_base_url
from ..errors import CarmenAPIConfigError
from ..models import CloudServiceRegion
from .models import JsonWebKeySet, TokenResponse

__all__ = ["AuthClient", "AuthClientOptions", "TokenResponse", "JsonWebKeySet"]


@dataclass
class AuthClientOptions:
    """
    Options of :class:`AuthClient`.

    Attributes
    ----------
    api_key : str
        The Carmen Cloud API key to exchange for access tokens.
    endpoint : Optional[str]
        Overrides the API base URL (e.g. ``https://api.dev.carmencloud.com``).
    cloud_service_region : Optional[CloudServiceRegion]
        ``AUTO`` (default, latency-based routing), ``EU`` or ``US``.
    retry_count : Optional[int]
        How many times a failed request is retried. Default: 3.
    renew_before_expiry_seconds : int
        Renew the cached token this many seconds before it expires. Default: 60.
    """
    api_key: str
    endpoint: Optional[str] = None
    cloud_service_region: Optional[Union[CloudServiceRegion, str]] = None
    retry_count: Optional[int] = 3
    renew_before_expiry_seconds: int = 60


class AuthClient:
    """
    Exchanges an API key for short-lived (60-minute) bearer access tokens and
    caches the current token until shortly before it expires. Thread-safe.
    """

    def __init__(self, options: AuthClientOptions):
        if not options.api_key:
            raise CarmenAPIConfigError("api_key must be specified.")
        self.options = options
        self.base_url = select_api_base_url(options.endpoint, options.cloud_service_region) + "/auth"
        self.session = create_session(options.retry_count)
        self._token: Optional[TokenResponse] = None
        self._lock = threading.Lock()

    def get_access_token(self, force_refresh: bool = False) -> TokenResponse:
        """Returns a valid access token, requesting a new one when the cached one is missing or expiring."""
        with self._lock:
            if force_refresh or self._token is None or self._is_expiring(self._token):
                self._token = self.create_access_token()
            return self._token

    def create_access_token(self) -> TokenResponse:
        """Requests a new access token, bypassing the cache."""
        response = self.session.post(self.base_url + "/token", headers={"x-api-key": self.options.api_key})
        raise_for_status(response)
        return TokenResponse.model_validate(response.json())

    def get_jwks(self) -> JsonWebKeySet:
        """Fetches the public keys that verify the issued tokens (RS256 JWTs)."""
        response = self.session.get(self.base_url + "/.well-known/jwks.json")
        raise_for_status(response)
        return JsonWebKeySet.model_validate(response.json())

    def _is_expiring(self, token: TokenResponse) -> bool:
        return token.expires_at - self.options.renew_before_expiry_seconds <= time.time()
