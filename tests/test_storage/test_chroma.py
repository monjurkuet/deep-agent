"""
Tests for ChromaDB storage backend.
"""

import pytest
from deep_agent.storage.chroma import ChromaStorage, initialize_chroma
from deep_agent.core.exceptions import BackendError


def test_chroma_initialization():
    """Test ChromaDB initialization."""
    storage = ChromaStorage(persist_directory="./test_data/chroma")
    storage.initialize()
    assert storage.client is not None
    storage.close()
    print("✓ ChromaDB initialized successfully")


def test_get_collection():
    """Test getting a collection."""
    storage = initialize_chroma("./test_data/chroma")
    collection = storage.get_collection("test_collection")
    assert collection.name == "test_collection"
    storage.close()
    print("✓ Collection created/retrieved successfully")


def test_uninitialized_error():
    """Test error when using uninitialized storage."""
    storage = ChromaStorage()

    with pytest.raises(BackendError):
        storage.get_collection("test")
    print("✓ Uninitialized error test passed")
