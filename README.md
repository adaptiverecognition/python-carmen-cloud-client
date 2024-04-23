# Carmen Cloud Client by Adaptive Recognition

Python client for [Carmen Cloud](https://carmencloud.com/) by [Adaptive Recognition](https://adaptiverecognition.com/). This unified library provides you with access to both the **Vehicle API** and the **Transportation & Cargo API**.

## Supported API Versions

- Vehicle API: v1.4
- Transportation & Cargo API: v1.0

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

### 📦 Storage & Hook API

```python
from carmen_cloud_client import StorageAndHookAPIClient, StorageAndHookAPIOptions

options = StorageAndHookAPIOptions(
    api_key="<YOUR_API_KEY>",
    cloud_service_region="EU"
)
client = StorageAndHookAPIClient(options)

# List Events
events = client.get_events("vehicle")
print("events:", events)

# Get Storage Status
status = client.get_storage_status()
print("status:", status)

# Update Storage Status
updated_status = client.update_storage_status(transport=True)
print('updatedStatus:', updated_status)

# Create Hook
created_hook = client.create_hook(
    hook_url='https://your-domain.com/your-hook-path',
    apis=['vehicle', 'transport']
)
print('createdHook:', created_hook)

# List Hooks
hooks = client.get_hooks()
print('hooks:', hooks)

# Get Hook
hook = client.get_hook('https://your-domain.com/your-hook-path')
print('hook:', hook)

# Update Hook
updated_hook = client.update_hook(
    'https://your-domain.com/your-hook-path',
    vehicle=True, transport=True
)
print('updatedHook:', updated_hook)

# Delete Hook
client.delete_hook('https://your-domain.com/your-hook-path')
```

## 🔧 Development

For more information about developing and contributing to this project, see [DEVELOPMENT.md](DEVELOPMENT.md).
