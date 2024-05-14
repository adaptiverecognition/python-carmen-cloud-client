#!/usr/bin/env bash

aws apigateway get-model --rest-api-id jw68bdy2t5 --model-name Response | jq --raw-output '.schema' > ./assets/vehicle/response.schema.json
aws apigateway get-model --rest-api-id 2bzr9vm131 --model-name Response | jq --raw-output '.schema' > ./assets/transport/response.schema.json

aws apigateway get-model --rest-api-id 24ut7ue8d8 --model-name APIStorageStatusRequest | jq --raw-output '.schema' > ./assets/storage-and-hook/APIStorageStatusRequest.schema.json
aws apigateway get-model --rest-api-id 24ut7ue8d8 --model-name CreateHookRequest | jq --raw-output '.schema' > ./assets/storage-and-hook/CreateHookRequest.schema.json
aws apigateway get-model --rest-api-id 24ut7ue8d8 --model-name EventsResponse | jq --raw-output '.schema' > ./assets/storage-and-hook/EventsResponse.schema.json
aws apigateway get-model --rest-api-id 24ut7ue8d8 --model-name Hook | jq --raw-output '.schema' > ./assets/storage-and-hook/Hook.schema.json
aws apigateway get-model --rest-api-id 24ut7ue8d8 --model-name Hooks | jq --raw-output '.schema' > ./assets/storage-and-hook/Hooks.schema.json
aws apigateway get-model --rest-api-id 24ut7ue8d8 --model-name OKResponse | jq --raw-output '.schema' > ./assets/storage-and-hook/OKResponse.schema.json
aws apigateway get-model --rest-api-id 24ut7ue8d8 --model-name StorageStatusResponse | jq --raw-output '.schema' > ./assets/storage-and-hook/StorageStatusResponse.schema.json
aws apigateway get-model --rest-api-id 24ut7ue8d8 --model-name UpdateHookRequest | jq --raw-output '.schema' > ./assets/storage-and-hook/UpdateHookRequest.schema.json

aws apigateway get-model --rest-api-id yqh6c9omp7 --model-name APIListResponse | jq --raw-output '.schema' > ./assets/descriptor/APIListResponse.schema.json
aws apigateway get-model --rest-api-id yqh6c9omp7 --model-name DimensionListReponse | jq --raw-output '.schema' > ./assets/descriptor/DimensionListReponse.schema.json
aws apigateway get-model --rest-api-id yqh6c9omp7 --model-name PaidSubscriptionListResponse | jq --raw-output '.schema' > ./assets/descriptor/PaidSubscriptionListResponse.schema.json
aws apigateway get-model --rest-api-id yqh6c9omp7 --model-name PaidSubscriptionUsageResponse | jq --raw-output '.schema' > ./assets/descriptor/PaidSubscriptionUsageResponse.schema.json
aws apigateway get-model --rest-api-id yqh6c9omp7 --model-name ProductsResponse | jq --raw-output '.schema' > ./assets/descriptor/ProductsResponse.schema.json
aws apigateway get-model --rest-api-id yqh6c9omp7 --model-name UsagePlanListResponse | jq --raw-output '.schema' > ./assets/descriptor/UsagePlanListResponse.schema.json
aws apigateway get-model --rest-api-id yqh6c9omp7 --model-name UsagePlanSubscriptionListResponse | jq --raw-output '.schema' > ./assets/descriptor/UsagePlanSubscriptionListResponse.schema.json
aws apigateway get-model --rest-api-id yqh6c9omp7 --model-name Prices | jq --raw-output '.schema' > ./assets/descriptor/Prices.schema.json
aws apigateway get-model --rest-api-id yqh6c9omp7 --model-name UsagePlanUsageResponse | jq --raw-output '.schema' > ./assets/descriptor/UsagePlanUsageResponse.schema.json

for file in $(find ./assets/storage-and-hook -name '*.json'); do
    # replace the remote reference with the local one
    sed -i 's|https://apigateway.amazonaws.com/restapis/'"24ut7ue8d8"'/models/\(.*\)"|\1.schema.json"|g' "$file"
done