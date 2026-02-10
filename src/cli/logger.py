"""Logging configuration."""

import logging
import sys
from typing import Optional

from cli.config import get_config


def setup_logging(
    name: Optional[str] = None, level: Optional[str] = None
) -> logging.Logger:
    """Setup logging configuration.

    Args:
        name: Logger name (usually __name__)
        level: Log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)

    Returns:
        Configured logger instance.
    """
    config = get_config()
    log_level = level or config.log_level

    logger = logging.getLogger(name or __name__)
    logger.setLevel(getattr(logging, log_level))

    # Remove existing handlers
    logger.handlers = []

    # Console handler
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(getattr(logging, log_level))

    # Formatter
    if config.debug:
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
    else:
        formatter = logging.Formatter("%(levelname)s - %(message)s")

    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger
