"""Tests for configuration module."""

import os
import pytest
from cli.config import Config, get_config


def test_config_default_env():
    """Test config with default environment."""
    config = Config()
    assert config.env in ["dev", "test", "prod"]


def test_config_dev_env():
    """Test config with dev environment."""
    config = Config(env="dev")
    assert config.env == "dev"
    assert config.debug is True
    assert config.log_level == "DEBUG"


def test_config_test_env():
    """Test config with test environment."""
    config = Config(env="test")
    assert config.env == "test"
    assert config.debug is True
    assert config.log_level == "DEBUG"


def test_config_prod_env():
    """Test config with prod environment."""
    config = Config(env="prod")
    assert config.env == "prod"
    assert config.debug is False
    assert config.log_level == "INFO"


def test_get_config_singleton():
    """Test get_config returns singleton."""
    cfg1 = get_config("dev")
    cfg2 = get_config()
    assert cfg1 is cfg2


def test_config_attributes():
    """Test config has all required attributes."""
    config = Config(env="test")
    assert hasattr(config, "env")
    assert hasattr(config, "debug")
    assert hasattr(config, "log_level")
    assert hasattr(config, "api_base_url")
    assert hasattr(config, "timeout")
    assert hasattr(config, "max_retries")
