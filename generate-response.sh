#!/usr/bin/env bash

datamodel-codegen --input-file-type jsonschema --input assets/transport/response.schema.json --output carmen_cloud_client/transport/response.py
datamodel-codegen --input-file-type jsonschema --input assets/vehicle/response.schema.json --output carmen_cloud_client/vehicle/response.py

datamodel-codegen --input-file-type jsonschema --input assets/storage-and-hook/APIStorageStatusRequest.schema.json --output carmen_cloud_client/storage_and_hook/api_storage_status_request.py
datamodel-codegen --input-file-type jsonschema --input assets/storage-and-hook/CreateHookRequest.schema.json --output carmen_cloud_client/storage_and_hook/create_hook_request.py
datamodel-codegen --input-file-type jsonschema --input assets/storage-and-hook/EventsResponse.schema.json --output carmen_cloud_client/storage_and_hook/events_response.py
datamodel-codegen --input-file-type jsonschema --input assets/storage-and-hook/Hook.schema.json --output carmen_cloud_client/storage_and_hook/hook.py
datamodel-codegen --input-file-type jsonschema --input assets/storage-and-hook/Hooks.schema.json --output carmen_cloud_client/storage_and_hook/hooks.py
datamodel-codegen --input-file-type jsonschema --input assets/storage-and-hook/OKResponse.schema.json --output carmen_cloud_client/storage_and_hook/ok_response.py
datamodel-codegen --input-file-type jsonschema --input assets/storage-and-hook/StorageStatusResponse.schema.json --output carmen_cloud_client/storage_and_hook/storage_status_response.py
datamodel-codegen --input-file-type jsonschema --input assets/storage-and-hook/UpdateHookRequest.schema.json --output carmen_cloud_client/storage_and_hook/update_hook_request.py

datamodel-codegen --input-file-type jsonschema --input assets/descriptor/APIListResponse.schema.json --output carmen_cloud_client/descriptor/api-list-response.py
datamodel-codegen --input-file-type jsonschema --input assets/descriptor/DimensionListReponse.schema.json --output carmen_cloud_client/descriptor/dimension-list-response.py
datamodel-codegen --input-file-type jsonschema --input assets/descriptor/PaidSubscriptionListResponse.schema.json --output carmen_cloud_client/descriptor/paid-subscription-list-response.py
datamodel-codegen --input-file-type jsonschema --input assets/descriptor/PaidSubscriptionUsageResponse.schema.json --output carmen_cloud_client/descriptor/paid-subscription-usage-response.py
datamodel-codegen --input-file-type jsonschema --input assets/descriptor/ProductsResponse.schema.json --output carmen_cloud_client/descriptor/products-response.py
datamodel-codegen --input-file-type jsonschema --input assets/descriptor/UsagePlanListResponse.schema.json --output carmen_cloud_client/descriptor/usage-plan-list-response.py
datamodel-codegen --input-file-type jsonschema --input assets/descriptor/UsagePlanSubscriptionListResponse.schema.json --output carmen_cloud_client/descriptor/usage-plan-subscription-list-response.py
datamodel-codegen --input-file-type jsonschema --input assets/descriptor/Prices.schema.json --output carmen_cloud_client/descriptor/prices.py
datamodel-codegen --input-file-type jsonschema --input assets/descriptor/UsagePlanUsageResponse.schema.json --output carmen_cloud_client/descriptor/usage-plan-usage-response.py
