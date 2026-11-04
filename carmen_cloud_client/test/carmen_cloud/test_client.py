import json
import time

import pytest
import responses
from responses import matchers

from carmen_cloud_client import (
    AuthClient,
    AuthClientOptions,
    CarmenAPIConfigError,
    CarmenAPIError,
    CarmenCloudClient,
    CarmenCloudClientOptions,
)

BASE = "https://api.test.carmencloud.com"


def token(value="t1", workspace_id="ws-1", expires_in=3600):
    return {
        "access_token": value, "workspace_id": workspace_id, "expires_at": int(time.time()) + expires_in,
        "expires_in": expires_in, "role": "ADMIN", "scope": f"cc.workspace.admin.{workspace_id}",
        "token_type": "Bearer",
    }


def client(**kwargs):
    return CarmenCloudClient(CarmenCloudClientOptions(api_key="key-1", endpoint=BASE, retry_count=0, **kwargs))


def bearer(value):
    return [matchers.header_matcher({"Authorization": f"Bearer {value}"})]


@responses.activate
def test_auth_exchanges_and_caches_token():
    rsp = responses.post(f"{BASE}/auth/token", json=token(), match=[matchers.header_matcher({"x-api-key": "k"})])
    auth = AuthClient(AuthClientOptions(api_key="k", endpoint=BASE, retry_count=0))
    assert auth.get_access_token().access_token == "t1"
    assert auth.get_access_token().access_token == "t1"
    assert rsp.call_count == 1


@responses.activate
def test_auth_renews_expiring_token():
    responses.post(f"{BASE}/auth/token", json=token("old", expires_in=30))
    responses.post(f"{BASE}/auth/token", json=token("new"))
    auth = AuthClient(AuthClientOptions(api_key="k", endpoint=BASE, retry_count=0))
    assert auth.get_access_token().access_token == "old"
    assert auth.get_access_token().access_token == "new"


@responses.activate
def test_auth_invalid_key_raises():
    responses.post(f"{BASE}/auth/token", status=403,
                   json={"error": "invalid_client", "error_description": "Unknown API key."})
    auth = AuthClient(AuthClientOptions(api_key="bad", endpoint=BASE, retry_count=0))
    with pytest.raises(CarmenAPIError) as e:
        auth.get_access_token()
    assert e.value.status == 403
    assert str(e.value) == "Unknown API key."


@responses.activate
def test_auth_jwks():
    responses.get(f"{BASE}/auth/.well-known/jwks.json", json={"keys": [{"kid": "k1", "kty": "RSA"}]})
    auth = AuthClient(AuthClientOptions(api_key="k", endpoint=BASE, retry_count=0))
    assert auth.get_jwks().keys[0].kid == "k1"


def test_requires_credential():
    with pytest.raises(CarmenAPIConfigError):
        CarmenCloudClient(CarmenCloudClientOptions(endpoint=BASE))


def test_requires_workspace_with_access_token():
    with pytest.raises(CarmenAPIConfigError):
        CarmenCloudClient(CarmenCloudClientOptions(access_token="t", endpoint=BASE))


@responses.activate
def test_uses_key_workspace_and_bearer():
    responses.post(f"{BASE}/auth/token", json=token("t1", "ws-42"))
    responses.get(f"{BASE}/workspace/ws-42", json={"workspaceId": "ws-42", "name": "Acme", "owner": "u1"},
                  match=bearer("t1"))
    assert client().workspace.get().name == "Acme"


@responses.activate
def test_access_token_callable():
    responses.delete(f"{BASE}/workspace/ws-9", json={"message": "deleted"}, match=bearer("user"))
    c = CarmenCloudClient(CarmenCloudClientOptions(access_token=lambda: "user", workspace_id="ws-9", endpoint=BASE))
    assert c.workspace.delete().message == "deleted"


@responses.activate
def test_renews_token_once_when_rejected():
    responses.post(f"{BASE}/auth/token", json=token("stale"))
    responses.post(f"{BASE}/auth/token", json=token("fresh"))
    responses.get(f"{BASE}/workspace/ws-1/storage/status", status=403, json={"message": "Forbidden"},
                  match=bearer("stale"))
    responses.get(f"{BASE}/workspace/ws-1/storage/status", json={"enabledApis": {"vehicle": True}, "topicArn": None},
                  match=bearer("fresh"))
    status = client().storage.get_status()
    assert status.enabledApis == {"vehicle": True}
    assert status.topicArn is None


@responses.activate
def test_api_error():
    responses.post(f"{BASE}/auth/token", json=token())
    responses.get(f"{BASE}/workspace/ws-1/user/u-404", status=404, json={"message": "No such user."})
    with pytest.raises(CarmenAPIError) as e:
        client().members.get("u-404")
    assert e.value.status == 404
    assert str(e.value) == "No such user."


@responses.activate
def test_hook_url_is_one_path_segment():
    responses.post(f"{BASE}/auth/token", json=token())
    responses.patch(f"{BASE}/workspace/ws-1/storage/hooks/https%3A%2F%2Fexample.com%2Fhook",
                    match=[matchers.json_params_matcher({"vehicle": False})],
                    json={"hookUrl": "https://example.com/hook", "apis": {"vehicle": False}, "protocol": "https",
                          "status": "confirmed", "topicArn": "arn", "topicName": "t"})
    assert client().hooks.update("https://example.com/hook", {"vehicle": False}).hookUrl == "https://example.com/hook"


@responses.activate
def test_query_parameters():
    responses.post(f"{BASE}/auth/token", json=token())
    responses.get(f"{BASE}/workspace/ws-1/events/vehicle",
                  match=[matchers.query_param_matcher({"limit": "10", "order": "desc"})],
                  json={"events": [], "continuationToken": None})
    page = client().events.list("vehicle", limit=10, order="desc")
    assert page.events == []
    assert page.continuationToken is None


@responses.activate
def test_list_all_api_keys():
    key = {"workspaceId": "ws-1", "name": "n", "value": "v"}
    responses.post(f"{BASE}/auth/token", json=token())
    responses.get(f"{BASE}/workspace/ws-1/apikey", match=[matchers.query_param_matcher({"limit": "1"})],
                  json={"list": [{**key, "apiKeyId": "a"}], "lastKey": "a"})
    responses.get(f"{BASE}/workspace/ws-1/apikey",
                  match=[matchers.query_param_matcher({"limit": "1", "last_key": "a"})],
                  json={"list": [{**key, "apiKeyId": "b"}], "lastKey": None})
    assert [k.apiKeyId for k in client().api_keys.list_all(limit=1)] == ["a", "b"]


@responses.activate
def test_api_key_roles_outside_documented_enum():
    # The API returns roles the spec does not list (e.g. a lowercase legacy `owner`).
    key = {"workspaceId": "ws-1", "name": "n", "value": "v", "apiKeyId": "a"}
    responses.post(f"{BASE}/auth/token", json=token())
    responses.get(f"{BASE}/workspace/ws-1/apikey",
                  json={"list": [{**key, "role": "ADMIN"}, {**key, "role": "owner"}], "lastKey": None})
    assert [k.role for k in client().api_keys.list().list_] == ["ADMIN", "owner"]


@responses.activate
def test_request_bodies():
    responses.post(f"{BASE}/auth/token", json=token())
    responses.post(f"{BASE}/workspace/ws-1/apikey", match=[matchers.json_params_matcher({"name": "ci", "role": "EDITOR"})],
                   json={"apiKeyId": "k", "name": "ci", "value": "secret", "workspaceId": "ws-1", "role": "EDITOR"})
    responses.post(f"{BASE}/workspace/ws-1/user", match=[matchers.json_params_matcher({"email": "a@b.c"})],
                   json={"workspaceId": "ws-1", "email": "a@b.c", "role": "EDITOR", "status": "pending", "message": "ok"})
    responses.delete(f"{BASE}/workspace/ws-1/apikey/k", body="")
    c = client()
    assert c.api_keys.create({"name": "ci", "role": "EDITOR"}).value == "secret"
    assert c.members.invite("a@b.c").status.value == "pending"
    assert c.api_keys.delete("k") is None
