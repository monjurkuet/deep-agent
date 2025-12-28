# Architecture Documentation

## Overview

The Deep Research Agent is built on [DeepAgents](https://github.com/langchain-ai/deepagents), providing a production-grade framework for autonomous research with built-in planning, filesystem management, and subagent capabilities.

## System Architecture

### Components

```
┌─────────────────────────────────────────────────────────┐
│                     Application Layer                     │
│  ┌─────────────┐    ┌─────────────┐               │
│  │  main.py    │    │  test_agent.py│               │
│  └─────────────┘    └─────────────┘               │
└─────────────────────────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────┐
│                  Core Agent Layer                     │
│  ┌──────────────────────────────────────────┐       │
│  │          AgentFactory (agent.py)       │       │
│  │  - Model creation                     │       │
│  │  - Backend setup                     │       │
│  │  - Checkpointer configuration         │       │
│  └──────────────────────────────────────────┘       │
│                          │                               │
│  ┌───────────────────────┼───────────────────────┐   │
│  │                       │                       │   │
│  ▼                       ▼                       ▼   │
│  ┌──────────┐      ┌──────────┐      ┌──────────┐ │
│  │ DeepAgents│      │Ollama    │      │LangGraph │ │
│  │ Runtime  │◄─────│ Models   │      │Checkpt  │ │
│  └──────────┘      └──────────┘      └──────────┘ │
└─────────────────────────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────┐
│                  Configuration Layer                    │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐   │
│  │ settings  │  │  models  │  │constants │   │
│  └──────────┘  └──────────┘  └──────────┘   │
└─────────────────────────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────┐
│                   Storage Layer                         │
│  ┌──────────┐      ┌──────────┐                      │
│  │ChromaDB  │      │ StateBackend│                      │
│  └──────────┘      └──────────┘                      │
└─────────────────────────────────────────────────────────┘
```

## Module Details

### Config Layer (`src/deep_agent/config/`)

**Purpose**: Centralized configuration management with type safety.

**Components**:
- `settings.py`: Pydantic-based settings loaded from environment variables
- `models.py`: Pydantic models for configuration validation
- `constants.py`: Default values and system prompts

**Design Decisions**:
- Uses `pydantic-settings` for environment variable loading
- Nested config structure (Ollama, Backend, Logging)
- Validation at startup (e.g., log levels)

### Core Layer (`src/deep_agent/core/`)

**Purpose**: Agent initialization and orchestration logic.

**Components**:
- `agent.py`: `AgentFactory` for creating Deep Agents
- `exceptions.py`: Custom exception hierarchy
- `middleware.py`: Observability middleware for logging

**Design Decisions**:
- Factory pattern for agent creation
- Separation of concerns (model creation, backend setup)
- Observability middleware hooks for monitoring

### Storage Layer (`src/deep_agent/storage/`)

**Purpose**: Abstraction for different storage backends.

**Components**:
- `base.py`: Abstract interface for storage backends
- `chroma.py`: ChromaDB implementation for semantic search
- `composite.py`: Factory for composite backends

**Design Decisions**:
- Abstract base class for type safety
- Pluggable backend architecture
- Error handling with custom exceptions

### Tools Layer (`src/deep_agent/tools/`)

**Purpose**: Custom tool implementations (Phase 2+).

**Components**:
- `base.py`: Base class for all tools

**Design Decisions**:
- Extensible tool architecture
- Consistent interface for all tools

## Data Flow

### Agent Invocation Flow

```
User Query
    │
    ▼
Agent.invoke(message, config)
    │
    ├─► Load config from Settings
    ├─► Create model (Ollama)
    ├─► Setup backend (StateBackend)
    ├─► Configure checkpointer (MemorySaver)
    │
    ▼
DeepAgents Runtime
    │
    ├─► Planning (write_todos)
    ├─► Tool execution (ls, read_file, write_file, etc.)
    ├─► LLM inference
    ├─► Context management
    │
    ▼
Response to user
```

### Storage Flow

```
Application
    │
    ▼
StorageBackend (abstract)
    │
    ├─► ChromaStorage (persistent semantic search)
    │       └─► ChromaDB (./data/chroma)
    │
    └─► StateBackend (ephemeral file system)
            └─► LangGraph state (in-memory)
```

## Configuration

### Environment Variables

| Variable | Default | Description |
|----------|----------|-------------|
| `OLLAMA_BASE_URL` | `http://localhost:11434` | Ollama API endpoint |
| `OLLAMA_PLANNING_MODEL_NAME` | `ministral-3:latest` | Model for planning tasks |
| `OLLAMA_EXECUTION_MODEL_NAME` | `ministral-3:latest` | Model for execution tasks |
| `OLLAMA_PLANNING_TEMPERATURE` | `0.7` | Temperature for planning (higher creativity) |
| `OLLAMA_EXECUTION_TEMPERATURE` | `0.0` | Temperature for execution (more deterministic) |
| `LOG_LEVEL` | `INFO` | Logging verbosity |

## Error Handling

### Exception Hierarchy

```
DeepAgentError (base)
    ├─► ModelError (model-related)
    ├─► BackendError (storage-related)
    ├─► ToolError (tool-related)
    └─► ConfigurationError (config-related)
```

### Error Recovery

- Model errors: Logged and re-raised with context
- Backend errors: Graceful degradation where possible
- Configuration errors: Fail fast at startup

## Testing Strategy

### Test Structure

```
tests/
├── conftest.py           # Shared fixtures
├── test_config/           # Configuration tests
├── test_core/             # Core agent tests
└── test_storage/          # Storage backend tests
```

### Test Categories

1. **Unit Tests**: Individual module functionality
2. **Integration Tests**: Module interactions
3. **End-to-End Tests**: Full workflow scenarios

### Running Tests

```bash
# All tests
uv run pytest tests/ -v

# With coverage
uv run pytest tests/ --cov=src/deep_agent

# Specific module
uv run pytest tests/test_core/ -v
```

## Future Enhancements

### Phase 2: Custom Tools
- Browser tool (Playwright)
- Scraper tool (Crawl4AI)
- Semantic search tool (ChromaDB)
- Graph query tool (GraphRAG)

### Phase 3: Advanced Features
- Specialized subagents
- Composite backend for hybrid storage
- GraphRAG integration

### Phase 4: Production Features
- Rate limiting
- Human-in-the-loop checkpoints
- Output validation
