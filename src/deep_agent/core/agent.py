"""
Agent factory and initialization logic.
"""

import uuid
from typing import Optional
from langchain_ollama import ChatOllama
from langgraph.checkpoint.memory import MemorySaver
from deepagents import create_deep_agent
from deepagents.backends import StateBackend
from deep_agent.config.settings import Settings
from deep_agent.config.models import AgentConfig, ModelConfig
from deep_agent.config.constants import DEFAULT_AGENT_CONFIG
from deep_agent.core.exceptions import ModelError, ConfigurationError
from deep_agent.utils.logging import setup_logging
from deep_agent.tools.registry import get_available_tools
from loguru import logger


class AgentFactory:
    """Factory for creating Deep Agents with proper configuration."""

    def __init__(self, settings: Optional[Settings] = None):
        self.settings = settings or Settings()
        setup_logging(self.settings.logging_config)

    def _create_model(self, config: ModelConfig):
        """Create a LangChain model from configuration."""
        if config.provider != "ollama":
            raise ConfigurationError(f"Unsupported model provider: {config.provider}")

        try:
            model = ChatOllama(
                model=config.model_name,
                temperature=config.temperature,
                base_url=self.settings.ollama.base_url,
            )
            logger.info(f"Created Ollama model: {config.model_name}")
            return model
        except Exception as e:
            raise ModelError(f"Failed to create model: {e}")

    def _create_backend(self):
        """Create filesystem backend based on configuration."""
        backend_type = self.settings.backend.type

        if backend_type == "state":

            def backend_factory(runtime):
                return StateBackend(runtime)

            logger.debug("Using StateBackend for filesystem")
            return backend_factory
        else:
            raise ConfigurationError(f"Unsupported backend type: {backend_type}")

    def create_agent(
        self,
        config: Optional[AgentConfig] = None,
    ):
        """Create a Deep Agent with specified configuration."""
        config = config or DEFAULT_AGENT_CONFIG

        try:
            # Create model
            model = self._create_model(config.model)

            # Create backend
            backend = self._create_backend()

            # Get custom tools
            custom_tools = get_available_tools()
            logger.info(
                f"Loaded {len(custom_tools)} custom tools: {[t.name for t in custom_tools]}"
            )

            # Create checkpointer
            checkpointer = None
            if config.checkpointer_enabled:
                checkpointer = MemorySaver()
                logger.debug("Enabled checkpointer with MemorySaver")

            agent = create_deep_agent(
                model=model,
                system_prompt=config.system_prompt,
                backend=backend,
                checkpointer=checkpointer,
                tools=custom_tools,
            )

            logger.info("Deep Agent created successfully")
            return agent

        except Exception as e:
            logger.error(f"Failed to create agent: {e}")
            raise

    def create_config_for_thread(self, thread_id: Optional[str] = None) -> dict:
        """Create config dict for a thread."""
        if thread_id is None:
            thread_id = str(uuid.uuid4())
        return {"configurable": {"thread_id": thread_id}}


# Convenience function
def create_agent(settings: Optional[Settings] = None) -> tuple:
    """
    Create an agent and a new thread config.

    Returns:
        tuple: (agent, config) where config contains thread_id
    """
    factory = AgentFactory(settings)
    agent = factory.create_agent()
    config = factory.create_config_for_thread()
    return agent, config
