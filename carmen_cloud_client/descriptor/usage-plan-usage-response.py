# generated by datamodel-codegen:
#   filename:  UsagePlanUsageResponse.schema.json
#   timestamp: 2024-05-14T11:10:00+00:00

from __future__ import annotations

from datetime import date

from pydantic import BaseModel


class UsagePlanQuotaUsage(BaseModel):
    startDate: date
    endDate: date
