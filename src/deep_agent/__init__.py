"""Deep Research Agent package.

A production-grade research agent built with DeepAgents and Ollama.
"""

from deep_agent.config.settings import Settings
from deep_agent.config.constants import (
    DEFAULT_AGENT_CONFIG,
    DEFAULT_EXECUTION_MODEL,
    DEFAULT_PLANNING_MODEL,
    DEFAULT_SYSTEM_PROMPT,
)
from deep_agent.core.agent import AgentFactory, create_agent
from deep_agent.storage.chroma import ChromaStorage, initialize_chroma

__version__ = "0.1.0"
__all__ = [
    "Settings",
    "DEFAULT_AGENT_CONFIG",
    "DEFAULT_PLANNING_MODEL",
    "DEFAULT_EXECUTION_MODEL",
    "DEFAULT_SYSTEM_PROMPT",
    "AgentFactory",
    "create_agent",
    "ChromaStorage",
    "initialize_chroma",
]
