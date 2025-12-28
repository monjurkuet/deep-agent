"""
Tests for composite backend with long-term memory.
"""

import pytest
from deep_agent import create_agent
from deep_agent.config.settings import Settings


def test_default_backend_type():
    """Test default backend type is 'state'."""
    settings = Settings()
    assert settings.backend.type == "state"
    assert settings.backend.routes is None
    print("✓ Default backend type test passed")


def test_backend_with_routes():
    """Test backend with routes configuration."""
    settings = Settings(
        backend={
            "type": "composite",
            "routes": {"/memories/": None},  # Will be StoreBackend factory
        }
    )

    assert settings.backend.type == "composite"
    assert "/memories/" in settings.backend.routes
    print("✓ Backend with routes test passed")


def test_create_agent_with_composite_backend():
    """Test creating agent with composite backend."""
    from deep_agent.config.settings import BackendConfig

    settings = Settings(
        backend=BackendConfig(
            type="composite",
            routes={"/memories/": None},
        )
    )

    agent, config = create_agent(settings)

    assert agent is not None
    assert "thread_id" in config["configurable"]
    print("✓ Agent creation with composite backend test passed")


def test_create_agent_with_state_backend():
    """Test creating agent with state backend."""
    agent, config = create_agent()

    assert agent is not None
    assert "thread_id" in config["configurable"]
    print("✓ Agent creation with state backend test passed")


if __name__ == "__main__":
    # Run all tests
    test_default_backend_type()
    test_backend_with_routes()
    test_create_agent_with_composite_backend()
    test_create_agent_with_state_backend()
    print("\n✅ All composite backend tests passed!")
