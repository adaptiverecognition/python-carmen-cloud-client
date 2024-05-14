# generated by datamodel-codegen:
#   filename:  UsagePlanSubscriptionListResponse.schema.json
#   timestamp: 2024-05-14T11:09:59+00:00

from __future__ import annotations

from typing import List

from pydantic import BaseModel, Field


class UsagePlanIds(BaseModel):
    __root__: List[str] = Field(
        ...,
        description='The list of usage plan IDs the authenticated user is subscribed to.',
        title='Usage Plan IDs',
    )
