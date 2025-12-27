"""
Configuration management using Pydantic settings.
Loads from environment variables with validation.
"""

from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class OllamaConfig(BaseModel):
    """Ollama model configuration."""

    base_url: str = "http://localhost:11434"
    planning_model: str = "ministral-3:latest"
    execution_model: str = "ministral-3:latest"
    timeout: int = 300
    temperature_planning: float = 0.0
    temperature_execution: float = 0.1


class BackendConfig(BaseModel):
    """Backend configuration."""

    type: str = "state"
    persist_directory: str = "./data/chroma"


class LoggingConfig(BaseModel):
    """Logging configuration."""

    level: str = "INFO"
    format: str = "{time:YYYY-MM-DD HH:mm:ss} | {level} | {name}:{function}:{line} - {message}"
    file_path: str | None = None


class Settings(BaseSettings):
    """Application settings."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    ollama: OllamaConfig = Field(default_factory=OllamaConfig)
    backend: BackendConfig = Field(default_factory=BackendConfig)
    logging_config: LoggingConfig = Field(default_factory=LoggingConfig)
