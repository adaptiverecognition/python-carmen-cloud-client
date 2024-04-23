# generated by datamodel-codegen:
#   filename:  CreateHookRequest.schema.json
#   timestamp: 2024-04-23T13:27:51+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class Apis(BaseModel):
    vehicle: Optional[bool] = Field(
        None,
        description='Optional. Indicates whether to enable storage for the Vehicle API.',
    )
    transport: Optional[bool] = Field(
        None,
        description='Optional. Indicates whether to enable storage for the Transport API.',
    )


class CreateHookRequest(BaseModel):
    hookUrl: str = Field(..., description='The URL of the hook.')
    apis: Apis = Field(
        ...,
        description='An object with properties that correspond to API subscriptions.',
    )
