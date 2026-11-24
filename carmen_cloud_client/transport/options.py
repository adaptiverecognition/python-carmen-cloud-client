from dataclasses import dataclass
from typing import Optional
from enum import Enum
from ..models import CloudServiceRegion

class CodeType(Enum):
    """
    The type of code to read.
    """
    ISO = "iso"
    TRUCK = "truck"
    AM_RAIL = "am-rail"
    EU_RAIL = "eu-rail"

@dataclass
class TransportAPIOptions:
    """
    Options for configuring the TransportAPI client.

    Attributes
    ----------
    disable_iso_code : Optional[bool]
        Deprecated: use ``disable_additional_code``. Legacy additional-code
        switch for the ``iso`` and ``eu-rail`` code types; sends
        ``X-Disable-Iso-Code``. On OCR engines from ``7.3.20.46`` it is only a
        fallback, used when ``disable_additional_code`` is not set.
    disable_checksum_check : Optional[bool]
        Deprecated: sends the legacy ``X-Disable-Checksum-Check`` header, kept
        for older OCR engines. From ``7.3.20.46`` the engine handles checksum
        checks internally and this option has no effect.
    enable_full_us_accr_code : Optional[bool]
        Enables full US ACCR code recognition; sends
        ``X-Enable-Full-Us-Accr-Code``. Applies only to the ``truck`` code type.
    disable_additional_code : Optional[bool]
        Disables additional code reading (such as the ISO equipment/type code)
        for the ``iso`` and ``eu-rail`` code types; sends
        ``X-Disable-Additional-Code``. Supported by OCR engines from
        ``7.3.20.46``. When set (``True`` or ``False``) it takes precedence over
        ``disable_iso_code``. ``None`` (the default) sends nothing.
    """
    api_key: str
    type: CodeType
    endpoint: Optional[str] = None
    cloud_service_region: Optional[CloudServiceRegion] = None
    disable_iso_code: Optional[bool] = False
    disable_checksum_check: Optional[bool] = False
    enable_full_us_accr_code: Optional[bool] = False
    disable_image_resizing: Optional[bool] = False
    enable_wide_range_analysis: Optional[bool] = False
    max_reads: Optional[int] = 1
    retry_count: Optional[int] = 2
    disable_additional_code: Optional[bool] = None
