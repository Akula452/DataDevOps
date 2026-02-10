"""Conftest for pytest configuration."""

import os
import sys
from pathlib import Path

# Add src directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

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
    # Save original values
    original_env = os.environ.get("ENVIRONMENT")
    original_log_level = os.environ.get("LOG_LEVEL")

    # Set test environment
    os.environ["ENVIRONMENT"] = "test"
    # Remove LOG_LEVEL to allow config to use defaults
    os.environ.pop("LOG_LEVEL", None)

    yield

    # Restore original values
    if original_env is not None:
        os.environ["ENVIRONMENT"] = original_env
    else:
        os.environ.pop("ENVIRONMENT", None)

    if original_log_level is not None:
        os.environ["LOG_LEVEL"] = original_log_level
    else:
        os.environ.pop("LOG_LEVEL", None)
