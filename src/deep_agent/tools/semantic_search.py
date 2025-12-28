"""
Semantic search tool using ChromaDB and Ollama embeddings.
"""

from typing import Optional
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from loguru import logger


def semantic_search(
    query: str,
    collection_name: str = "default",
    n_results: int = 5,
) -> str:
    """Search for documents by semantic similarity.

    Args:
        query: Search query text
        collection_name: Collection to search in
        n_results: Number of results to return

    Returns:
        Formatted search results
    """
    try:
        embeddings = OllamaEmbeddings(model="nomic-embed-text:latest")
        vectorstore = Chroma(
            persist_directory="./data/chroma",
            collection_name=collection_name,
            embedding_function=embeddings,
        )

        results = vectorstore.similarity_search_with_score(query, k=n_results)

        if not results:
            return f"No results found in collection '{collection_name}' for query: '{query}'"

        formatted = [
            f"[Result {i + 1}] (Score: {1 - score:.4f})\n{doc.page_content}\n"
            for i, (doc, score) in enumerate(results)
        ]

        logger.info(f"Found {len(results)} results for query in '{collection_name}'")
        return f"Found {len(results)} results:\n\n" + "\n".join(formatted)
    except Exception as e:
        logger.error(f"Failed to search semantic index: {e}")
        return f"Error searching: {str(e)}"


def add_to_search_index(
    texts: list[str],
    collection_name: str = "default",
    metadata: Optional[list[dict]] = None,
) -> str:
    """Add documents to semantic search index.

    Args:
        texts: List of text documents to add
        collection_name: Name of the collection to add to
        metadata: Optional list of metadata dicts for each text

    Returns:
        Success message with count
    """
    if not texts:
        return "No documents to add (empty list provided)"

    try:
        embeddings = OllamaEmbeddings(model="nomic-embed-text:latest")
        vectorstore = Chroma(
            persist_directory="./data/chroma",
            collection_name=collection_name,
            embedding_function=embeddings,
        )

        vectorstore.add_texts(texts=texts, metadatas=metadata)

        logger.info(f"Added {len(texts)} documents to collection '{collection_name}'")
        return f"Successfully added {len(texts)} documents to search index (collection: {collection_name})"
    except Exception as e:
        logger.error(f"Failed to add documents to search index: {e}")
        return f"Error adding documents: {str(e)}"


def list_search_collections() -> str:
    """List all collections in the search index.

    Returns:
        Formatted list of collections
    """
    try:
        embeddings = OllamaEmbeddings(model="nomic-embed-text:latest")
        vectorstore = Chroma(
            persist_directory="./data/chroma",
            collection_name="default",
            embedding_function=embeddings,
        )

        client = vectorstore._client
        collections = client.list_collections()

        if not collections:
            return "No collections found in search index"

        collection_info = []
        for col in collections:
            count = col.count()
            collection_info.append(f"- {col.name}: {count} documents")

        logger.info(f"Listed {len(collections)} collections")
        return "Collections in search index:\n" + "\n".join(collection_info)
    except Exception as e:
        logger.error(f"Failed to list collections: {e}")
        return f"Error listing collections: {str(e)}"
