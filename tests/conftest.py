"""Conftest for pytest configuration."""

import os
import pytest
from cli.config import Config


@pytest.fixture
def config_dev():
    """Provide dev config."""
    return Config(env="dev")


@pytest.fixture
def config_test():
    """Provide test config."""
    return Config(env="test")


@pytest.fixture(autouse=True)
def set_test_env():
    """Set environment to test for all tests."""
    os.environ["ENVIRONMENT"] = "test"
    yield
    os.environ.pop("ENVIRONMENT", None)
