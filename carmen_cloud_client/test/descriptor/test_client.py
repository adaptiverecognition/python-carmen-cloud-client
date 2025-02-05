from carmen_cloud_client import (
    DescriptorAPIClient,
    DescriptorAPIOptions
)
from carmen_cloud_client.errors import CarmenAPIConfigError
from dotenv import load_dotenv
from io import BytesIO
from packaging import version
import os
import pytest

load_dotenv()

# configure environment
api_key = os.getenv("TEST_DEV_API_KEY", "")
endpoint = os.getenv("TEST_DEV_ENDPOINT_URL", "")
eu_prod_api_key = os.getenv("TEST_EU_PROD_API_KEY", "")
us_prod_api_key = os.getenv("TEST_US_PROD_API_KEY", "")

test_options = DescriptorAPIOptions(
    api_key=api_key,
    endpoint=endpoint
)

def test_invalid_cloud_service_region_throws():
    invalid_options = DescriptorAPIOptions(
        api_key=api_key,
        cloud_service_region="INVALID",
    )
    with pytest.raises(CarmenAPIConfigError):
        DescriptorAPIClient(invalid_options)

def test_get_apis_returns_a_valid_response():
    client = DescriptorAPIClient(test_options)
    apis = client.get_apis()

    assert apis is not None
