"""
Application constants and default values.
"""

from deep_agent.config.models import AgentConfig, ModelConfig

# System prompts
DEFAULT_SYSTEM_PROMPT = """You are a research assistant with access to a file system.

## Your Tools:
- write_todos: Plan and track research tasks
- ls, read_file, write_file, edit_file: Manage notes and documents
- glob, grep: Search through your files

## Research Workflow:
1. Use write_todos to break down research question
2. Save your findings to files in file system
3. Synthesize information into coherent reports

Start by creating a plan using write_todos, then execute it step by step.
"""

# Default model configurations
DEFAULT_PLANNING_MODEL = ModelConfig(
    provider="ollama",
    model_name="ministral-3:latest",
    temperature=0.0,
    timeout=300,
)

DEFAULT_EXECUTION_MODEL = ModelConfig(
    provider="ollama",
    model_name="ministral-3:latest",
    temperature=0.1,
    timeout=300,
)

# Default agent configuration
DEFAULT_AGENT_CONFIG = AgentConfig(
    model=DEFAULT_PLANNING_MODEL,
    system_prompt=DEFAULT_SYSTEM_PROMPT,
    checkpointer_enabled=True,
    backend_type="state",
)
