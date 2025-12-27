"""
Abstract storage interface for type safety.
"""

from abc import ABC, abstractmethod
from typing import Any


class StorageBackend(ABC):
    """Abstract base class for storage backends."""

    @abstractmethod
    def initialize(self) -> None:
        """Initialize storage backend."""
        pass

    @abstractmethod
    def get_collection(self, name: str) -> Any:
        """Get or create a collection by name."""
        pass

    @abstractmethod
    def close(self) -> None:
        """Close connections and cleanup."""
        pass
