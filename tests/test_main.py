"""Tests for CLI main module."""

from click.testing import CliRunner
from cli.main import cli


def test_cli_help():
    """Test CLI help output."""
    runner = CliRunner()
    result = runner.invoke(cli, ["--help"])
    assert result.exit_code == 0
    assert "DataDevOps CLI" in result.output


def test_cli_with_dev_env():
    """Test CLI with dev environment."""
    runner = CliRunner()
    result = runner.invoke(cli, ["--env", "dev", "health", "status"])
    assert result.exit_code == 0
    assert "dev" in result.output
    assert "healthy" in result.output.lower()


def test_cli_with_test_env():
    """Test CLI with test environment."""
    runner = CliRunner()
    result = runner.invoke(cli, ["--env", "test", "health", "status"])
    assert result.exit_code == 0
    assert "test" in result.output
    assert "healthy" in result.output.lower()


def test_cli_with_debug():
    """Test CLI with debug flag."""
    runner = CliRunner()
    result = runner.invoke(cli, ["--debug", "health", "status"])
    assert result.exit_code == 0
