import inspect
import os

import pytest
from dotenv import load_dotenv

load_dotenv()


def pytest_configure(config):
    config.addinivalue_line("markers", "integration: calls a live Carmen Cloud API (needs TEST_* API keys)")


def pytest_collection_modifyitems(config, items):
    """Tests that send a recognition request are integration tests: skip them without API keys."""
    have_keys = bool(os.getenv("TEST_DEV_API_KEY"))
    skip = pytest.mark.skip(reason="TEST_DEV_API_KEY is not set")
    for item in items:
        source = inspect.getsource(item.function) if hasattr(item, "function") else ""
        if "response = client.send" in source:
            item.add_marker(pytest.mark.integration)
            if not have_keys:
                item.add_marker(skip)
