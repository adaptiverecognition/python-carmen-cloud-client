#!/usr/bin/env bash
# Regenerates the pydantic (v2) models from the JSON schemas / OpenAPI documents in assets/.
set -euo pipefail
common=(--output-model-type pydantic_v2.BaseModel --target-python-version 3.10 --disable-timestamp --use-standard-collections)

datamodel-codegen "${common[@]}" --input-file-type jsonschema --input assets/transport/response.schema.json --output carmen_cloud_client/transport/response.py
datamodel-codegen "${common[@]}" --input-file-type jsonschema --input assets/vehicle/response.schema.json --output carmen_cloud_client/vehicle/response.py
datamodel-codegen "${common[@]}" --input-file-type openapi --input assets/carmen-cloud/carmen-cloud.json --output carmen_cloud_client/carmen_cloud/models.py --use-title-as-name --field-constraints
datamodel-codegen "${common[@]}" --input-file-type openapi --input assets/carmen-cloud/authentication.json --output carmen_cloud_client/auth/models.py
