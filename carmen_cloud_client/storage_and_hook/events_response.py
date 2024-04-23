# generated by datamodel-codegen:
#   filename:  EventsResponse.schema.json
#   timestamp: 2024-04-23T13:27:51+00:00

from __future__ import annotations

from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


class Event(BaseModel):
    event: Dict[str, Any] = Field(
        ...,
        description='The original event object, preserving the structure as it would have been returned by the API.',
    )
    attachmentURLs: List[str] = Field(
        ...,
        description='An array of URLs where the images sent with the original request can be downloaded.',
    )
    creationTimestamp: float = Field(
        ...,
        description='The millisecond-based Unix timestamp of the time the event was created.',
    )
    api: str = Field(
        ...,
        description='The API the event originates from. At the time of writing this documentation, the available APIs were `vehicle` and `transport` (Vehicle API and Transportation & Cargo API).',
    )


class EventsResponse(BaseModel):
    events: List[Event] = Field(
        ..., description='A list of events that match the query parameters'
    )
    continuationToken: Optional[str] = Field(
        None,
        description='A token that can be passed in the query parameter `continuation-token` in the next request to continue pagination after the last event in the current batch.',
    )
