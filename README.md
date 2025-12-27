# Deep Research Agent

Production-grade autonomous research agent built with [DeepAgents](https://github.com/langchain-ai/deepagents) and [Ollama](https://ollama.com/).

[![Python 3.12+](https://img.shields.io/badge/python-3.12%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: ruff](https://img.shields.io/badge/code%20style-ruff-FF0066.svg)](https://github.com/astral-sh/ruff)

## Features

- 🧠 Planning with built-in `write_todos` tool
- 📁 Filesystem management (read, write, edit, search)
- 🔄 Multi-turn conversation persistence
- 🎯 Tiered model approach (671B cloud for planning, 8B local for execution)
- 🌐 Web scraping with Crawl4AI (fast content extraction)
- 🌐 Browser automation with Playwright (full web interaction)
- 🗃️ ChromaDB integration for semantic search (Phase 2+)
- 🕸️ GraphRAG for multi-hop reasoning (Phase 3)

## Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/your-username/deep-agent.git
cd deep-agent

# Install dependencies with uv
uv sync

# Install package in development mode
uv pip install -e .
```

### Prerequisites

1. **Install Ollama**:
   ```bash
   # macOS
   brew install ollama

   # Linux
   curl -fsSL https://ollama.com/install.sh | sh
   ```

2. **Start Ollama**:
   ```bash
   ollama serve
   ```

3. **Install dependencies**:
   ```bash
   uv sync
   uv pip install -e ".[dev]"
   ```

4. **Configure environment**:
   ```bash
   cp .env.example .env
   # Edit .env with your settings (if needed)
   ```

### Usage

```bash
# Create agent
from deep_agent import create_agent

agent, config = create_agent()

# Use tools (will be integrated with agent in Phase 2.3)
result = agent.invoke({"messages": [{"role": "user", "content": "Research a topic"}]}, config=config)

# Run tests
./scripts/run_tests.sh

# Or with pytest
uv run pytest tests/ -v
```

### Available Tools (Phase 2)

### Web Automation

**Crawl4AI Scraper** (`web_scraper`)
- Fast content extraction from web pages
- Returns markdown or text format
- Best for: Articles, docs, blog posts

**Playwright Browser** (7 tools)
- Full browser automation (click, type, navigate)
- Best for: Forms, logins, complex SPAs
- Tools:
  - `navigate_browser` - Navigate to URLs
  - `click_element` - Click elements by CSS selector
  - `extract_text` - Extract page text
  - `extract_hyperlinks` - Extract links
  - `get_elements` - Get elements by selector
  - `current_webpage` - Get current page URL
  - `previous_webpage` - Navigate back

**All tools are automatically integrated with DeepAgents agent!**

### Usage Example

```python
from deep_agent import create_agent

# Create agent with all tools loaded automatically
agent, config = create_agent()

# Make a request that uses tools
result = agent.invoke({
    "messages": [{
        "role": "user",
        "content": "Scrape https://example.com and tell me the title"
    }]
}, config=config)

print(result["messages"][-1].content)
```

## Documentation

- [Full Documentation](docs/) - All project documentation
- [Session History](docs/sessions/) - Development session logs
- [Architecture](docs/architecture.md) - System architecture details
- [Contributing](CONTRIBUTING.md) - How to contribute
- [Changelog](CHANGELOG.md) - Version history and changes

## Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## Development

### Project Structure

```
deep-agent/
├── src/deep_agent/    # Main package
│   ├── config/        # Configuration layer
│   ├── core/          # Agent logic
│   ├── storage/       # Storage backends
│   ├── tools/         # Tools (Phase 2+)
│   └── utils/         # Utilities
├── tests/             # Test suite
├── scripts/           # Helper scripts
└── docs/              # Documentation
```

### Running Tests

```bash
# All tests
uv run pytest tests/ -v

# With coverage
uv run pytest tests/ --cov=src/deep_agent --cov-report=html

# Specific test file
uv run pytest tests/test_core/test_agent.py -v
```

### Linting

```bash
# Format code
uv run black src/ tests/

# Lint
uv run ruff check src/ tests/

# Type checking
uv run mypy src/
```

## License

MIT
