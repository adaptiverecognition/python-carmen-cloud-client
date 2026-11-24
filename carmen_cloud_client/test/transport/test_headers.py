"""Unit tests (no live API): the option-to-header mapping of the Transport client."""
from carmen_cloud_client import TransportAPIClient, TransportAPIOptions, CodeType


def headers_for(**options):
    client = TransportAPIClient(TransportAPIOptions(api_key="key", type=CodeType.ISO, endpoint="https://api.test", **options))
    return client.create_headers("multipart/form-data")


def test_omits_additional_code_header_by_default():
    headers = headers_for(disable_iso_code=True)
    assert "x-disable-additional-code" not in headers
    assert headers["x-disable-iso-code"] == "true"


def test_sends_disable_additional_code_true():
    assert headers_for(disable_additional_code=True)["x-disable-additional-code"] == "true"


def test_sends_explicit_false_alongside_the_deprecated_iso_switch():
    headers = headers_for(disable_additional_code=False, disable_iso_code=True)
    assert headers["x-disable-additional-code"] == "false"
