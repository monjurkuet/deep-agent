"""
Tests for configuration settings.
"""

from deep_agent.config.settings import Settings


def test_default_settings():
    """Test that default settings are created correctly."""
    settings = Settings()

    assert settings.ollama.base_url == "http://localhost:11434"
    assert settings.ollama.planning_model_name == "ministral-3:latest"
    assert settings.ollama.execution_model_name == "ministral-3:latest"
    assert settings.ollama.planning_temperature == 0.7
    assert settings.ollama.execution_temperature == 0.0
    assert settings.backend.type == "state"
    assert settings.logging_config.level == "INFO"


def test_valid_log_levels():
    """Test that default log level is set correctly."""
    settings = Settings()
    assert settings.logging_config.level == "INFO"
