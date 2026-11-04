# Carmen Cloud Client by Adaptive Recognition

Python client for [Carmen Cloud](https://carmencloud.com/) by [Adaptive Recognition](https://adaptiverecognition.com/). This unified library provides you with access to the **Vehicle API**, the **Transportation & Cargo API** and the **Carmen Cloud API** (workspaces, API keys, billing, usage, stored events, storage and hooks).

## Supported API Versions

- Vehicle API: v1.4.2
- Transportation & Cargo API: v1.0.1
- Carmen Cloud API: current latest version

## 🛠️ How to Install

```sh
pip install carmen-cloud-client
```

## 🚀 Usage

You can utilize either the Vehicle API or the Transportation & Cargo API based on your needs.

### 🚗 Vehicle API

```python
from carmen_cloud_client import VehicleAPIClient, VehicleAPIOptions, SelectedServices, Locations

options = VehicleAPIOptions(
    api_key="<YOUR_API_KEY>",
    services=SelectedServices(anpr=True, mmr=True),
    input_image_location=Locations.Europe.Hungary,
    cloud_service_region="EU"
)
client = VehicleAPIClient(options)

response = client.send("./car.jpg")
print(response)
```

### 🚚 Transportation & Cargo API

```python
from carmen_cloud_client import TransportAPIClient, TransportAPIOptions, CodeType

options = TransportAPIOptions(
    api_key="<YOUR_API_KEY>",
    type=CodeType.ISO,
    cloud_service_region="EU"
)
client = TransportAPIClient(options)

response = client.send("./container.jpg")
print(response)
```

### ☁️ Carmen Cloud API

Manage your workspace programmatically: members, API keys, billing, usage
reports, stored events, event storage and webhooks. Use an API key with a
workspace role (`ADMIN`, `EDITOR` or `ACCOUNTANT`); the client exchanges it for
short-lived bearer tokens and renews them automatically.

```python
from carmen_cloud_client import CarmenCloudClient, CarmenCloudClientOptions

client = CarmenCloudClient(CarmenCloudClientOptions(api_key="<YOUR_API_KEY>"))

workspace = client.workspace.get()
print(workspace.name, workspace.subscriptions)

# API keys
key = client.api_keys.create({"name": "ci", "role": "EDITOR"})
for k in client.api_keys.list_all():
    print(k.name)
client.api_keys.rotate(key.apiKeyId)

# Usage (YYYY-MM-DD)
usage = client.usage.get_workspace_usage(from_="2026-10-01", to="2026-10-31")
print(usage.totalQuantity)

# Members
client.members.invite("colleague@example.com", role="ACCOUNTANT")

# Event storage and webhooks
client.storage.update_status({"vehicle": True})
client.hooks.create("https://example.com/carmen-hook", {"vehicle": True})
page = client.events.list("vehicle", limit=10, order="desc")
print(len(page.events))
```

| Attribute | Operations |
| --- | --- |
| `workspace` | `get`, `rename`, `delete`\*, `transfer_ownership`\* |
| `members` | `list`, `invite`, `get`, `update_role`, `remove` |
| `api_keys` | `list`, `list_all`, `create`, `get`, `update`, `rotate`, `delete` |
| `billing` | `update_subscription`, `update_billing_profile`, `create_auth_session`, `create_portal_session`, `preview_invoice`, `update_usage_cap`\* |
| `usage` | `get_workspace_usage`, `get_api_key_usage` |
| `events` | `list` |
| `storage` | `get_status`, `update_status` |
| `hooks` | `list`, `create`, `get`, `update`, `delete` |

\* Requires a signed-in user's session token instead of an API key: pass
`access_token` (a string or a function returning one) and `workspace_id`
instead of `api_key`.

Responses are pydantic models (`carmen_cloud_client.carmen_cloud.models`).
Failed calls raise `CarmenAPIError` with the HTTP `status` and the API's error
message. To get a bearer token for your own HTTP client, use
`AuthClient(AuthClientOptions(api_key=...)).get_access_token()`.

### Upgrading from 1.x

- `StorageAndHookAPIClient` is replaced by `CarmenCloudClient` (`storage`,
  `hooks` and `events`).
- Models are pydantic 2 models (use `model_dump()` instead of `dict()`).
- HTTP errors raise `CarmenAPIError` instead of `requests.HTTPError`.
- Python 3.10 or newer is required.

## 🔧 Development

For more information about developing and contributing to this project, see [DEVELOPMENT.md](DEVELOPMENT.md).
