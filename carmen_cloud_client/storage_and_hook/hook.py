# generated by datamodel-codegen:
#   filename:  Hook.schema.json
#   timestamp: 2024-05-10T13:30:47+00:00

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class Status(Enum):
    pending_confirmation = 'pending_confirmation'
    confirmed = 'confirmed'
    deleted = 'deleted'


class Protocol(Enum):
    http = 'http'
    https = 'https'


class Apis(BaseModel):
    vehicle: Optional[bool] = Field(
        None,
        description='Optional. Indicates whether to enable storage for the Vehicle API.',
    )
    transport: Optional[bool] = Field(
        None,
        description='Optional. Indicates whether to enable storage for the Transport API.',
    )


class Hook(BaseModel):
    status: Status = Field(..., description='The status of this hook')
    protocol: Protocol = Field(
        ..., description='The protocol used to send events to this hook.'
    )
    apis: Optional[Apis] = Field(
        None,
        description='An object with properties that correspond to API subscriptions.',
    )
    hookUrl: str = Field(
        ..., description='The URL of the webhook events will be sent to.'
    )
    topicName: str = Field(
        ...,
        description='The name of the AWS SNS topic that serves this hook. This can be used to verify incoming requests.',
    )
    topicArn: str = Field(
        ...,
        description='The ARN of the AWS SNS topic that serves this hook. This can be used to verify incoming requests.',
    )