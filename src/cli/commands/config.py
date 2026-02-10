"""Configuration command."""

import click
from cli.config import get_config
from cli.logger import setup_logging

logger = setup_logging(__name__)


@click.group()
def config() -> None:
    """Configuration management commands."""
    pass


@config.command()
@click.pass_context
def show(ctx: click.Context) -> None:
    """Show current configuration."""
    cfg = ctx.obj["config"]
    click.echo("Current Configuration:")
    click.echo(f"  Environment: {cfg.env}")
    click.echo(f"  Debug Mode: {cfg.debug}")
    click.echo(f"  Log Level: {cfg.log_level}")
    click.echo(f"  API Base URL: {cfg.api_base_url}")
    click.echo(f"  Request Timeout: {cfg.timeout}s")
    click.echo(f"  Max Retries: {cfg.max_retries}")


@config.command()
@click.option(
    "--env", type=click.Choice(["dev", "test", "prod"]), help="Switch environment"
)
@click.pass_context
def switch(ctx: click.Context, env: str) -> None:
    """Switch environment."""
    if not env:
        click.echo("Please specify an environment: --env {dev|test|prod}")
        return

    cfg = get_config(env)
    logger.info(f"Switched to {env} environment")
    click.echo(f"✓ Switched to {env} environment")
    click.echo(f"  API Base URL: {cfg.api_base_url}")
