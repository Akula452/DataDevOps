"""Main CLI entry point."""

import click
from cli.config import get_config
from cli.logger import setup_logging
from cli import commands

# Setup logger
logger = setup_logging(__name__)


@click.group()
@click.option(
    "--env",
    type=click.Choice(["dev", "test", "prod"]),
    default="dev",
    help="Environment to use",
)
@click.option("--debug/--no-debug", default=False, help="Enable debug mode")
@click.pass_context
def cli(ctx: click.Context, env: str, debug: bool) -> None:
    """DataDevOps CLI - Your data operations command-line tool."""
    # Initialize config
    config = get_config(env)
    ctx.ensure_object(dict)
    ctx.obj["config"] = config
    ctx.obj["debug"] = debug

    if debug:
        logger.setLevel("DEBUG")
        logger.debug(f"Debug mode enabled. Environment: {env}")


# Add command groups
cli.add_command(commands.health)
cli.add_command(commands.data)
cli.add_command(commands.config_cmd)


if __name__ == "__main__":
    cli(obj={})
