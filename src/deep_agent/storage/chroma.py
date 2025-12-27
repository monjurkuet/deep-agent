"""
ChromaDB storage backend for semantic search.
"""

import chromadb
from deep_agent.storage.base import StorageBackend
from deep_agent.core.exceptions import BackendError
from loguru import logger


class ChromaStorage(StorageBackend):
    """ChromaDB storage backend with proper error handling."""

    def __init__(self, persist_directory: str = "./data/chroma"):
        self.persist_directory = persist_directory
        self.client = None

    def initialize(self) -> None:
        """Initialize ChromaDB client."""
        try:
            self.client = chromadb.PersistentClient(path=self.persist_directory)
            logger.info(f"ChromaDB initialized: {self.persist_directory}")
        except Exception as e:
            raise BackendError(f"Failed to initialize ChromaDB: {e}")

    def get_collection(self, name: str) -> chromadb.Collection:
        """Get or create a collection by name."""
        if self.client is None:
            raise BackendError("ChromaDB not initialized. Call initialize() first.")

        try:
            collection = self.client.get_or_create_collection(name)
            logger.debug(f"Got collection: {name}")
            return collection
        except Exception as e:
            raise BackendError(f"Failed to get collection {name}: {e}")

    def close(self) -> None:
        """Cleanup ChromaDB client."""
        if self.client:
            logger.debug("Closing ChromaDB connection")
            self.client = None


def initialize_chroma(persist_directory: str = "./data/chroma") -> ChromaStorage:
    """Convenience function to initialize ChromaDB storage."""
    storage = ChromaStorage(persist_directory)
    storage.initialize()
    return storage
