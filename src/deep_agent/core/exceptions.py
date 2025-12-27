"""
Custom exceptions for Deep Research Agent.
"""

from typing import Any


class DeepAgentError(Exception):
    """Base exception for all Deep Agent errors."""

    def __init__(self, message: str, details: dict[str, Any] | None = None):
        self.message = message
        self.details = details or {}
        super().__init__(self.message)


class ModelError(DeepAgentError):
    """Exception raised for model-related errors."""

    pass


class BackendError(DeepAgentError):
    """Exception raised for backend-related errors."""

    pass


class ToolError(DeepAgentError):
    """Exception raised for tool-related errors."""

    pass


class ConfigurationError(DeepAgentError):
    """Exception raised for configuration errors."""

    pass
