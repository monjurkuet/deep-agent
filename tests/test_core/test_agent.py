"""
Tests for core agent functionality.
"""

import pytest
from deep_agent.core.exceptions import ConfigurationError
from deep_agent.config.models import ModelConfig, AgentConfig


def test_agent_creation(agent_factory):
    """Test that an agent can be created successfully."""
    agent = agent_factory.create_agent()
    assert agent is not None
    print("✓ Agent created successfully")


def test_agent_invoke_simple(agent_factory, config):
    """Test basic agent invocation."""
    agent = agent_factory.create_agent()
    result = agent.invoke(
        {"messages": [{"role": "user", "content": "Hello, who are you?"}]}, config=config
    )

    assert "messages" in result
    assert len(result["messages"]) > 0
    print("✓ Agent invoked successfully")


def test_planning_with_todos(agent_factory, config):
    """Test planning with write_todos tool."""
    agent = agent_factory.create_agent()
    result = agent.invoke(
        {
            "messages": [
                {"role": "user", "content": "Create a research plan for studying AI ethics"}
            ]
        },
        config=config,
    )

    assert "messages" in result
    response = result["messages"][-1].content
    print(f"✓ Planning test completed. Response: {response[:200]}...")


def test_file_operations(agent_factory, config):
    """Test file operations: write, read, list."""
    agent = agent_factory.create_agent()

    # Write file
    agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": "Write a file called test.txt with content 'Hello World'",
                }
            ]
        },
        config=config,
    )

    # List files
    agent.invoke({"messages": [{"role": "user", "content": "List all files"}]}, config=config)

    # Read file
    agent.invoke(
        {"messages": [{"role": "user", "content": "Read the contents of test.txt"}]}, config=config
    )

    print("✓ File operations test completed")


def test_multi_turn_persistence(agent_factory, config):
    """Test that conversation persists across turns."""
    agent = agent_factory.create_agent()

    # Turn 1: Write file
    agent.invoke(
        {
            "messages": [
                {"role": "user", "content": "Write a file called notes.md with 'Initial note'"}
            ]
        },
        config=config,
    )

    # Turn 2: Edit file (should remember it exists)
    agent.invoke(
        {"messages": [{"role": "user", "content": "Add 'Updated' to notes.md"}]}, config=config
    )

    # Turn 3: List files (should see notes.md)
    agent.invoke({"messages": [{"role": "user", "content": "List all files"}]}, config=config)

    print("✓ Multi-turn persistence test completed")


def test_file_search(agent_factory, config):
    """Test glob and grep tools."""
    agent = agent_factory.create_agent()

    # Create test files
    agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": "Create files: research.md and notes.txt with some content",
                }
            ]
        },
        config=config,
    )

    # Test glob
    agent.invoke(
        {"messages": [{"role": "user", "content": "Find all .md files using glob"}]}, config=config
    )

    # Test grep
    agent.invoke(
        {
            "messages": [
                {"role": "user", "content": "Search for word 'content' in all files using grep"}
            ]
        },
        config=config,
    )

    print("✓ File search test completed")


def test_invalid_model_provider(agent_factory):
    """Test error handling for invalid model provider."""
    invalid_config = AgentConfig(
        model=ModelConfig(provider="invalid", model_name="test"),
        system_prompt="Test prompt",
    )

    with pytest.raises(ConfigurationError):
        agent_factory.create_agent(invalid_config)
    print("✓ Invalid model provider test passed")
