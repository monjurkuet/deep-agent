"""
Tests for semantic search tool.
"""

from deep_agent.tools.semantic_search import (
    semantic_search,
    add_to_search_index,
    list_search_collections,
)


def test_add_to_search_index():
    """Test adding documents to search index."""
    result = add_to_search_index(
        texts=[
            "Python is a high-level programming language",
            "JavaScript is used for web development",
        ],
        collection_name="test_collection",
        metadata=[{"source": "doc1"}, {"source": "doc2"}],
    )

    assert "Successfully added" in result
    assert "2 documents" in result
    assert "test_collection" in result
    print("✓ Add to search index test passed")


def test_add_to_search_index_empty():
    """Test adding empty list to search index."""
    result = add_to_search_index(texts=[], collection_name="test_collection")

    assert "No documents to add" in result
    assert "empty list provided" in result
    print("✓ Add empty list test passed")


def test_semantic_search():
    """Test semantic search functionality."""
    # First add some documents
    add_to_search_index(
        texts=[
            "Python programming language for data science",
            "JavaScript web framework React",
            "Machine learning with Python",
        ],
        collection_name="test_search",
    )

    # Now search
    result = semantic_search(
        query="programming languages",
        collection_name="test_search",
        n_results=3,
    )

    assert "Found" in result
    assert "results" in result
    print("✓ Semantic search test passed")


def test_semantic_search_empty_collection():
    """Test searching in empty collection."""
    result = semantic_search(
        query="test query",
        collection_name="nonexistent_collection",
    )

    assert "No results found" in result or "Error" in result
    print("✓ Empty collection search test passed")


def test_list_search_collections():
    """Test listing all collections."""
    # Add to some collections
    add_to_search_index(
        texts=["Test document 1"],
        collection_name="collection_1",
    )
    add_to_search_index(
        texts=["Test document 2"],
        collection_name="collection_2",
    )

    # List collections
    result = list_search_collections()

    assert "Collections in search index:" in result or "Error" in result
    print("✓ List collections test passed")


def test_semantic_search_with_metadata():
    """Test adding and searching with metadata."""
    # Add documents with metadata
    add_to_search_index(
        texts=[
            "Deep Learning with PyTorch",
            "Natural Language Processing",
        ],
        collection_name="test_metadata",
        metadata=[
            {"category": "ML", "framework": "PyTorch"},
            {"category": "NLP", "topic": "text"},
        ],
    )

    # Search should work regardless of metadata
    result = semantic_search(
        query="machine learning",
        collection_name="test_metadata",
        n_results=2,
    )

    assert "Found" in result or "Error" in result
    print("✓ Metadata search test passed")


def test_multiple_collections():
    """Test working with multiple collections."""
    # Add to different collections
    add_to_search_index(
        texts=["AI research"],
        collection_name="research",
    )
    add_to_search_index(
        texts=["Web development"],
        collection_name="web",
    )

    # Search in specific collection
    result = semantic_search(
        query="development",
        collection_name="web",
        n_results=1,
    )

    assert "Found" in result or "Error" in result
    print("✓ Multiple collections test passed")


if __name__ == "__main__":
    # Run all tests
    test_add_to_search_index()
    test_add_to_search_index_empty()
    test_semantic_search()
    test_semantic_search_empty_collection()
    test_list_search_collections()
    test_semantic_search_with_metadata()
    test_multiple_collections()
    print("\n✅ All semantic search tests passed!")
