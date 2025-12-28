"""
Model configuration schemas for type safety.
"""

from pydantic import BaseModel, Field


class ModelConfig(BaseModel):
    provider: str = "ollama"
    model_name: str
    temperature: float = 0.0
    max_tokens: int | None = None
    timeout: int = 300


class AgentConfig(BaseModel):
    """Agent configuration."""

    model: ModelConfig
    system_prompt: str
    checkpointer_enabled: bool = True
    backend_type: str = "state"
    tools: list[str] = Field(default_factory=list)
    interrupt_before: dict[str, bool] = Field(default_factory=dict)
