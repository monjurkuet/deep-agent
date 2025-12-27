"""
Base tool class for future tool implementations.
"""

from typing import Any


class BaseTool:
    """Base class for all tools."""

    name: str
    description: str

    def __call__(self, *args, **kwargs) -> Any:
        """Execute the tool."""
        raise NotImplementedError
