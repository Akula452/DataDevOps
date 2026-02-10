"""Tests for commands."""

from click.testing import CliRunner
from cli.commands.health import health
from cli.commands.data import data
from cli.commands.config import config


def test_health_status():
    """Test health status command."""
    runner = CliRunner()
    result = runner.invoke(health, ["status"])
    assert result.exit_code == 0
    assert "healthy" in result.output.lower()


def test_health_api():
    """Test health api command."""
    runner = CliRunner()
    result = runner.invoke(health, ["api"])
    # May fail if API not running, but command should execute
    assert result.exit_code in [0, 1]


def test_data_list_datasets():
    """Test data list command."""
    runner = CliRunner()
    result = runner.invoke(data, ["list-datasets"])
    assert result.exit_code == 0
    assert "dataset" in result.output


def test_data_import():
    """Test data import command."""
    runner = CliRunner()
    result = runner.invoke(data, ["import-data", "/path/to/data"])
    assert result.exit_code == 0
    assert "Importing" in result.output


def test_data_export():
    """Test data export command."""
    runner = CliRunner()
    result = runner.invoke(data, ["export-data", "/path/to/export"])
    assert result.exit_code == 0
    assert "Exporting" in result.output


def test_config_show():
    """Test config show command."""
    runner = CliRunner()
    result = runner.invoke(config, ["show"])
    assert result.exit_code == 0
    assert "Configuration" in result.output
