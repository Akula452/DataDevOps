"""Health check command."""

import click
import requests
from cli.logger import setup_logging
from cli.config import get_config

logger = setup_logging(__name__)


@click.group()
def health() -> None:
    """Health check commands."""
    pass


@health.command()
@click.pass_context
def status(ctx: click.Context) -> None:
    """Check system health status."""
    config = ctx.obj["config"]
    click.echo(f"Environment: {config.env}")
    click.echo(f"Debug: {config.debug}")
    click.echo(f"API Base URL: {config.api_base_url}")
    click.echo("✓ CLI is healthy")


@health.command()
@click.pass_context
def api(ctx: click.Context) -> None:
    """Check API health."""
    config = ctx.obj["config"]
    try:
        response = requests.get(
            f"{config.api_base_url}/health",
            timeout=config.timeout
        )
        if response.status_code == 200:
            click.echo("✓ API is healthy")
        else:
            click.echo(f"✗ API returned status {response.status_code}", err=True)
    except requests.exceptions.RequestException as e:
        logger.error(f"API health check failed: {e}")
        click.echo(f"✗ API health check failed: {e}", err=True)
