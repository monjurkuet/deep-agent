"""
Factory for creating composite backends.
"""

from typing import Callable
from deepagents.backends import StateBackend, StoreBackend, CompositeBackend  # noqa: F401
from deep_agent.core.exceptions import BackendError
from loguru import logger


def create_composite_backend(
    routes: dict | None = None,
) -> Callable:
    """Create a composite backend factory with default StateBackend.

    Args:
        routes: Dictionary mapping path prefixes to backend factories
                 e.g., {"/memories/": lambda rt: StoreBackend(rt)}

    Returns:
        Factory function that creates CompositeBackend instance
    """
    default_routes = routes or {}

    def backend_factory(runtime):
        """Factory function that creates CompositeBackend instance."""
        try:
            backend = CompositeBackend(
                default=StateBackend(runtime),
                routes=default_routes,
            )
            logger.info(f"Created CompositeBackend with routes: {list(default_routes.keys())}")
            return backend
        except Exception as e:
            raise BackendError(f"Failed to create CompositeBackend: {e}")

    return backend_factory
