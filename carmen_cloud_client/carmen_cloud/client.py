"""Client for the Carmen Cloud API (``/workspace/{workspaceId}/...``)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable, Iterator, Optional, Type, TypeVar, Union
from urllib.parse import quote

from pydantic import BaseModel

from .._http import create_session, raise_for_status, select_api_base_url
from ..auth import AuthClient, AuthClientOptions
from ..errors import CarmenAPIConfigError, CarmenAPIError
from ..models import CloudServiceRegion
from .models import (
    ApiKey,
    ApiKeyPage,
    ApiKeyUsageReport,
    BillingAuthSession,
    BillingPortalSession,
    BillingProfile,
    BillingProfileRequest,
    CreateApiKeyRequest,
    CreateHookRequest,
    Hook,
    HookList,
    InvitationSentResult,
    InviteUserRequest,
    InvoicePreview,
    MessageResponse,
    StorageStatus,
    StoredEventPage,
    TransferResult,
    UpdateApiKeyRequest,
    UsageCapRequest,
    UsageCapResult,
    UsageReport,
    Workspace,
    WorkspaceUser,
    WorkspaceUserList,
)

M = TypeVar("M", bound=BaseModel)
Body = Union[BaseModel, dict]


@dataclass
class CarmenCloudClientOptions:
    """
    Options of :class:`CarmenCloudClient`.

    Attributes
    ----------
    api_key : Optional[str]
        A Carmen Cloud API key with a workspace role (``ADMIN``, ``EDITOR`` or
        ``ACCOUNTANT``). It is exchanged for short-lived bearer tokens
        automatically. Either this or ``access_token`` is required.
    access_token : Optional[Union[str, Callable[[], str]]]
        A bearer token, or a function returning one, used instead of an API key
        (e.g. a signed-in user's session token). The few operations marked
        "requires a user session" only work with such a token.
    workspace_id : Optional[str]
        The workspace to operate on. With ``api_key`` it defaults to the key's
        own workspace; with ``access_token`` it is required.
    endpoint : Optional[str]
        Overrides the API base URL (e.g. ``https://api.dev.carmencloud.com``).
    cloud_service_region : Optional[CloudServiceRegion]
        ``AUTO`` (default, latency-based routing), ``EU`` or ``US``.
    retry_count : Optional[int]
        How many times a failed request is retried. Default: 3.
    """
    api_key: Optional[str] = None
    access_token: Optional[Union[str, Callable[[], str]]] = None
    workspace_id: Optional[str] = None
    endpoint: Optional[str] = None
    cloud_service_region: Optional[Union[CloudServiceRegion, str]] = None
    retry_count: Optional[int] = 3


def _seg(value: str) -> str:
    return quote(value, safe="")


def _dump(body: Optional[Body]) -> Any:
    if isinstance(body, BaseModel):
        return body.model_dump(mode="json", by_alias=True, exclude_none=True)
    return body


class CarmenCloudClient:
    """
    A client for the Carmen Cloud API: workspace, members, API keys, billing,
    usage, stored events, storage settings and hooks.

    Example::

        client = CarmenCloudClient(CarmenCloudClientOptions(api_key="..."))
        workspace = client.workspace.get()
        for key in client.api_keys.list_all():
            print(key.name)
    """

    def __init__(self, options: CarmenCloudClientOptions):
        if not options.api_key and not options.access_token:
            raise CarmenAPIConfigError("Either api_key or access_token must be specified.")
        if options.access_token and not options.api_key and not options.workspace_id:
            raise CarmenAPIConfigError("workspace_id must be specified when using access_token.")
        self.options = options
        self.base_url = select_api_base_url(options.endpoint, options.cloud_service_region) + "/workspace"
        self.session = create_session(options.retry_count)
        self.auth: Optional[AuthClient] = None
        if options.api_key and not options.access_token:
            self.auth = AuthClient(AuthClientOptions(
                api_key=options.api_key,
                endpoint=options.endpoint,
                cloud_service_region=options.cloud_service_region,
                retry_count=options.retry_count,
            ))
        self.workspace = WorkspaceOperations(self)
        self.members = MemberOperations(self)
        self.api_keys = ApiKeyOperations(self)
        self.billing = BillingOperations(self)
        self.usage = UsageOperations(self)
        self.events = EventOperations(self)
        self.storage = StorageOperations(self)
        self.hooks = HookOperations(self)

    def get_workspace_id(self) -> str:
        """The workspace the client operates on."""
        if self.options.workspace_id:
            return self.options.workspace_id
        return self.auth.get_access_token().workspace_id

    def _bearer(self, force_refresh: bool) -> str:
        if self.auth:
            return self.auth.get_access_token(force_refresh).access_token
        token = self.options.access_token
        return token() if callable(token) else token

    def request(self, method: str, path: str, query: Optional[dict] = None, body: Optional[Body] = None) -> Any:
        """Sends a request to ``/workspace/{workspaceId}{path}`` and returns the parsed JSON body."""
        url = f"{self.base_url}/{_seg(self.get_workspace_id())}{path}"
        params = {k: v for k, v in (query or {}).items() if v is not None}
        json_body = _dump(body)

        def send(force_refresh: bool):
            headers = {"Authorization": f"Bearer {self._bearer(force_refresh)}"}
            response = self.session.request(method, url, params=params, json=json_body, headers=headers)
            raise_for_status(response)
            return response.json() if response.content else None

        try:
            return send(False)
        except CarmenAPIError as e:
            # The authorizer answers 401/403 for an expired token: renew a key-minted token once.
            if self.auth and e.status in (401, 403):
                return send(True)
            raise

    def _get(self, model: Type[M], method: str, path: str, **kwargs) -> M:
        return model.model_validate(self.request(method, path, **kwargs))


class _Operations:
    def __init__(self, client: CarmenCloudClient):
        self._client = client


class WorkspaceOperations(_Operations):
    """Workspace operations."""

    def get(self) -> Workspace:
        """Gets the workspace, enriched with its Stripe customer and subscriptions."""
        return self._client._get(Workspace, "GET", "")

    def rename(self, name: str) -> Workspace:
        """Renames the workspace (owner only)."""
        return self._client._get(Workspace, "PUT", "", body={"name": name})

    def delete(self) -> MessageResponse:
        """Deletes the workspace. Requires a user session (not an API-key token)."""
        return self._client._get(MessageResponse, "DELETE", "")

    def transfer_ownership(self, user_id: str) -> TransferResult:
        """Transfers ownership to another member. Requires a user session (not an API-key token)."""
        return self._client._get(TransferResult, "PATCH", f"/transfer/{_seg(user_id)}")


class MemberOperations(_Operations):
    """Workspace member and invitation operations."""

    def list(self, status: Optional[str] = None, role: Optional[str] = None,
             order_by: Optional[str] = None, order: Optional[str] = None) -> list[WorkspaceUser]:
        """Lists the members and pending invitations."""
        query = {"status": status, "role": role, "orderBy": order_by, "order": order}
        return self._client._get(WorkspaceUserList, "GET", "/user", query=query).root

    def invite(self, email: str, role: Optional[str] = None) -> InvitationSentResult:
        """Invites a user by email (role defaults to ``EDITOR``)."""
        body = InviteUserRequest(email=email, role=role)
        return self._client._get(InvitationSentResult, "POST", "/user", body=body)

    def get(self, user_id: str) -> WorkspaceUser:
        """Gets one member."""
        return self._client._get(WorkspaceUser, "GET", f"/user/{_seg(user_id)}")

    def update_role(self, user_id: str, role: str) -> MessageResponse:
        """Changes a member's role (``ADMIN``, ``EDITOR`` or ``ACCOUNTANT``)."""
        return self._client._get(MessageResponse, "PATCH", f"/user/{_seg(user_id)}", body={"role": role})

    def remove(self, user_id: str) -> MessageResponse:
        """Removes a member or revokes a pending invitation."""
        return self._client._get(MessageResponse, "DELETE", f"/user/{_seg(user_id)}")


class ApiKeyOperations(_Operations):
    """API key operations."""

    def list(self, limit: Optional[int] = None, search: Optional[str] = None,
             sort: Optional[str] = None, last_key: Optional[str] = None) -> ApiKeyPage:
        """Lists one page of API keys; pass the returned ``lastKey`` as ``last_key`` for the next page."""
        query = {"limit": limit, "search": search, "sort": sort, "last_key": last_key}
        return self._client._get(ApiKeyPage, "GET", "/apikey", query=query)

    def list_all(self, limit: Optional[int] = None, search: Optional[str] = None,
                 sort: Optional[str] = None) -> Iterator[ApiKey]:
        """Iterates over every API key, page by page."""
        last_key = None
        while True:
            page = self.list(limit=limit, search=search, sort=sort, last_key=last_key)
            yield from page.list_
            last_key = page.lastKey
            if not last_key:
                return

    def create(self, request: Union[CreateApiKeyRequest, dict]) -> ApiKey:
        """Creates an API key. The response carries the secret ``value``."""
        return self._client._get(ApiKey, "POST", "/apikey", body=request)

    def get(self, api_key_id: str) -> ApiKey:
        """Gets one API key."""
        return self._client._get(ApiKey, "GET", f"/apikey/{_seg(api_key_id)}")

    def update(self, api_key_id: str, request: Union[UpdateApiKeyRequest, dict]) -> ApiKey:
        """Updates an API key's name, role or product settings."""
        return self._client._get(ApiKey, "PUT", f"/apikey/{_seg(api_key_id)}", body=request)

    def rotate(self, api_key_id: str) -> ApiKey:
        """Issues a new secret value for the key and invalidates the old one."""
        return self._client._get(ApiKey, "PATCH", f"/apikey/{_seg(api_key_id)}")

    def delete(self, api_key_id: str) -> None:
        """Deletes an API key."""
        self._client.request("DELETE", f"/apikey/{_seg(api_key_id)}")


class BillingOperations(_Operations):
    """Billing operations (Stripe)."""

    def update_subscription(self, action: str, product_id: str, subscription_type: str) -> Workspace:
        """Applies a subscription change (subscribe, change or cancel a product subscription)."""
        query = {"action": action, "product_id": product_id, "subscription_type": subscription_type}
        return self._client._get(Workspace, "PATCH", "", query=query)

    def update_billing_profile(self, request: Union[BillingProfileRequest, dict]) -> BillingProfile:
        """Selects the billing account (locked after first use) and maintains invoice PO numbers."""
        return self._client._get(BillingProfile, "PUT", "/billing-profile", body=request)

    def create_auth_session(self, component: Optional[str] = None,
                            product_id: Optional[str] = None) -> BillingAuthSession:
        """Creates a Stripe customer session for embedded components (pricing table, buy button)."""
        query = {"component": component, "product_id": product_id}
        return self._client._get(BillingAuthSession, "GET", "/billing-auth-session", query=query)

    def create_portal_session(self, **options: Optional[str]) -> BillingPortalSession:
        """
        Creates a Stripe billing portal session; redirect the user to the returned ``url``.
        Keyword arguments are the query parameters: ``next_url``, ``type``,
        ``product_id``, ``subscription_type``, ``subscription_id``.
        """
        return self._client._get(BillingPortalSession, "GET", "/billing-portal-session", query=options)

    def update_usage_cap(self, request: Union[UsageCapRequest, dict]) -> UsageCapResult:
        """Turns the usage hard cap on or off. Requires a user session (not an API-key token)."""
        return self._client._get(UsageCapResult, "PUT", "/usage-cap", body=request)

    def preview_invoice(self, product_id: str) -> InvoicePreview:
        """Previews the next invoice of a metered subscription (``carmen`` or ``pr``)."""
        return self._client._get(InvoicePreview, "GET", "/invoice-preview", query={"product_id": product_id})


class UsageOperations(_Operations):
    """Usage reports. Dates are ``YYYY-MM-DD``."""

    def get_workspace_usage(self, from_: Optional[str] = None, to: Optional[str] = None) -> UsageReport:
        """Daily usage of the whole workspace."""
        return self._client._get(UsageReport, "GET", "/usage", query={"from": from_, "to": to})

    def get_api_key_usage(self, api_key_id: str, from_: Optional[str] = None,
                          to: Optional[str] = None) -> ApiKeyUsageReport:
        """Daily usage of one API key."""
        return self._client._get(ApiKeyUsageReport, "GET", f"/apikey/{_seg(api_key_id)}/usage",
                                 query={"from": from_, "to": to})


class EventOperations(_Operations):
    """Stored recognition events."""

    def list(self, api: str, limit: Optional[int] = None, order: Optional[str] = None,
             before: Optional[str] = None, after: Optional[str] = None,
             continuation_token: Optional[str] = None) -> StoredEventPage:
        """
        Lists stored events of a recognition API (``vehicle`` or ``transport``;
        storage must be enabled for it). Pass the returned ``continuationToken``
        as ``continuation_token`` for the next page.
        """
        query = {"limit": limit, "order": order, "before": before, "after": after,
                 "continuation-token": continuation_token}
        return self._client._get(StoredEventPage, "GET", f"/events/{_seg(api)}", query=query)


class StorageOperations(_Operations):
    """Event storage settings."""

    def get_status(self) -> StorageStatus:
        """Which APIs have event storage enabled, and the SNS topic events are published to."""
        return self._client._get(StorageStatus, "GET", "/storage/status")

    def update_status(self, apis: dict[str, bool]) -> StorageStatus:
        """Enables (``True``) or disables (``False``) event storage per API; omitted APIs are unchanged."""
        return self._client._get(StorageStatus, "PATCH", "/storage/status", body=apis)


class HookOperations(_Operations):
    """Webhook operations."""

    def list(self) -> list[Hook]:
        """Lists the registered hooks."""
        return self._client._get(HookList, "GET", "/storage/hooks").root

    def create(self, hook_url: str, apis: dict[str, bool]) -> Hook:
        """Registers a hook URL; the endpoint must confirm the SNS subscription."""
        return self._client._get(Hook, "POST", "/storage/hooks", body=CreateHookRequest(hookUrl=hook_url, apis=apis))

    def get(self, hook_url: str) -> Hook:
        """Gets one hook by its URL."""
        return self._client._get(Hook, "GET", f"/storage/hooks/{_seg(hook_url)}")

    def update(self, hook_url: str, apis: dict[str, bool]) -> Hook:
        """Changes which APIs' events are sent to the hook."""
        return self._client._get(Hook, "PATCH", f"/storage/hooks/{_seg(hook_url)}", body=apis)

    def delete(self, hook_url: str) -> None:
        """Deletes a hook."""
        self._client.request("DELETE", f"/storage/hooks/{_seg(hook_url)}")
