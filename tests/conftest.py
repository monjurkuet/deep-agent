"""
pytest configuration and shared fixtures.
"""

import pytest
from deep_agent.core.agent import AgentFactory


@pytest.fixture
def settings():
    """Create test settings with safe defaults."""
    from deep_agent.config.settings import Settings

    return Settings()


@pytest.fixture
def agent_factory(settings):
    """Create an AgentFactory instance."""
    return AgentFactory(settings)


@pytest.fixture
def config():
    """Create a test thread config."""
    import uuid

    return {"configurable": {"thread_id": str(uuid.uuid4())}}
