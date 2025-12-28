"""
Agent factory and initialization logic.
"""

from typing import Optional
import uuid
from langchain_ollama import ChatOllama
from langgraph.checkpoint.memory import MemorySaver
from langgraph.store.memory import InMemoryStore
from deepagents import create_deep_agent
from deepagents.backends import StateBackend, StoreBackend, CompositeBackend
from deep_agent.config.settings import Settings
from deep_agent.config.models import AgentConfig, ModelConfig
from deep_agent.config.constants import DEFAULT_SYSTEM_PROMPT
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

    def _create_backend_factory(self):
        """Create a backend factory based on configuration."""
        backend_type = self.settings.backend.type
        routes = self.settings.backend.routes

        if routes and backend_type == "composite":

            def backend_factory(runtime):
                backend = CompositeBackend(
                    default=StateBackend(runtime),
                    routes={"/memories/": StoreBackend(runtime), **routes},
                )
                logger.info(f"Created CompositeBackend with routes: {list(routes.keys())}")
                return backend

            return backend_factory

        elif backend_type == "state":

            def backend_factory(runtime):
                backend = StateBackend(runtime)
                logger.debug("Using StateBackend for filesystem")
                return backend

            return backend_factory

        else:
            raise ConfigurationError(f"Unsupported backend type: {backend_type}")

    def create_agent(
        self,
        config: Optional[AgentConfig] = None,
    ):
        """Create a Deep Agent with specified configuration."""

        try:
            # Create model from settings
            if config and config.model:
                model_config = config.model
            else:
                model_config = ModelConfig(
                    provider="ollama",
                    model_name=self.settings.ollama.execution_model_name,
                    temperature=self.settings.ollama.execution_temperature,
                )

            model = self._create_model(model_config)

            # Create checkpointer
            checkpointer = None
            checkpointer_enabled = config.checkpointer_enabled if config else True
            if checkpointer_enabled:
                checkpointer = MemorySaver()
                logger.debug("Enabled checkpointer with MemorySaver")

            # Create store for composite backend
            store = None
            if self.settings.backend.routes and self.settings.backend.type == "composite":
                store = InMemoryStore()
                logger.info("Created InMemoryStore for composite backend")

            # Get custom tools
            custom_tools = get_available_tools()
            tool_names = [t.name if hasattr(t, "name") else t.__name__ for t in custom_tools]
            logger.info(f"Loaded {len(custom_tools)} custom tools: {tool_names}")

            # Create agent
            agent_kwargs = {
                "model": model,
                "system_prompt": config.system_prompt if config else DEFAULT_SYSTEM_PROMPT,
                "backend": self._create_backend_factory(),
                "checkpointer": checkpointer,
                "tools": custom_tools,
            }

            if store is not None:
                agent_kwargs["store"] = store
                logger.info("Added store to agent for long-term memory")

            agent = create_deep_agent(**agent_kwargs)

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
