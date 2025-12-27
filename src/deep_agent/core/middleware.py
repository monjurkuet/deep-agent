"""
Logging utilities for observability.
"""

from loguru import logger


def log_agent_start():
    """Log agent initialization."""
    logger.info("Deep Agent initializing...")


def log_agent_ready(model_name: str):
    """Log when agent is ready."""
    logger.info(f"Deep Agent ready with model: {model_name}")


def log_invocation_start(message_count: int):
    """Log start of agent invocation."""
    logger.debug(f"Agent invocation started with {message_count} messages")


def log_invocation_complete(elapsed: float):
    """Log completion of agent invocation."""
    logger.info(f"Agent invocation completed in {elapsed:.2f}s")
