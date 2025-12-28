"""
Test that planning/execution model configuration works correctly.
"""

import pytest
from deep_agent.config.settings import Settings
from deep_agent.core.agent import AgentFactory
from deep_agent.config.models import ModelConfig


def test_default_values_used():
    """Test that defaults are used for planning/execution models."""
    
    settings = Settings()
    
    # Verify defaults
    assert settings.ollama.base_url == "http://localhost:11434"
    assert settings.ollama.planning_model_name == "ministral-3:latest"
    assert settings.ollama.execution_model_name == "ministral-3:latest"
    assert settings.ollama.planning_temperature == 0.7
    assert settings.ollama.execution_temperature == 0.0
    
    print("✓ Default values used correctly")


def test_agent_factory_uses_settings():
    """Test that AgentFactory correctly uses settings for model configuration."""
    
    # Create agent factory
    settings = Settings()
    factory = AgentFactory(settings)
    
    # Verify factory uses settings
    assert factory.settings.ollama.planning_model_name == "ministral-3:latest"
    assert factory.settings.ollama.execution_model_name == "ministral-3:latest"
    assert factory.settings.ollama.planning_temperature == 0.7
    assert factory.settings.ollama.execution_temperature == 0.0
    
    print("✓ AgentFactory correctly uses settings")


def test_model_config_has_temperature():
    """Test that ModelConfig has temperature field."""
    
    model_config = ModelConfig(
        provider="ollama",
        model_name="test-model",
        temperature=0.5,
    )
    
    assert model_config.temperature == 0.5
    
    print("✓ ModelConfig has temperature field")


def test_different_planning_execution_temperatures():
    """Test that planning and execution models can have different temperatures."""
    
    settings = Settings()
    
    # Planning should be higher (more creative)
    assert settings.ollama.planning_temperature >= 0.5
    
    # Execution should be lower (more deterministic)
    assert settings.ollama.execution_temperature <= 0.3
    
    print("✓ Planning/execution temperatures follow best practices")
