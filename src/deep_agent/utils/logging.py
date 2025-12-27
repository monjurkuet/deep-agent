"""
Logging configuration using loguru.
"""

import sys
from deep_agent.config.settings import LoggingConfig
from loguru import logger


def setup_logging(config: LoggingConfig) -> None:
    """Configure logging with loguru."""
    logger.remove()

    logger.add(
        sys.stdout,
        format=config.format,
        level=config.level,
        colorize=True,
    )

    if config.file_path:
        logger.add(
            config.file_path,
            format=config.format,
            level=config.level,
            rotation="10 MB",
            retention="7 days",
            compression="zip",
        )

    logger.info(f"Logging configured at {config.level} level")
