# Deep Agent - Interactive Chat Interface

Simple interactive chat interface for testing the Deep Agent with all features.

## Features

- **11 Tools**: Web scraper, browser automation, semantic search
- **Model Configuration**: Planning/execution models configurable via `.env`
- **Thread Persistence**: Conversations persist across sessions
- **Long-Term Memory** (Optional): Save important information across threads

## Usage

### Basic Chat (Ephemeral Storage)
```bash
uv run python chat.py
```

### Chat with Long-Term Memory (Composite Backend)
```bash
uv run python chat.py --composite
```

With composite backend:
- Files in `/memories/` persist across all threads
- Other files are ephemeral (lost when thread ends)
- Use `/memory` command to view saved information
- Use `/save` command to save conversation to memory

### Chat Commands

While in chat mode:
- Type normally to chat with the agent
- `quit` or `exit` - Exit the chat
- The agent has access to all tools automatically

## Features Demonstrated

### Built-in DeepAgents Tools
- `write_todos` - Plan and track tasks
- `ls` - List files
- `read_file` - Read files
- `write_file` - Create files
- `edit_file` - Edit files
- `task` - Spawn subagents

### Custom Tools
- **Web Scraper** (`web_scraper`)
  ```python
  Scrape https://example.com
  ```

- **Browser Automation** (7 tools)
  ```python
  Navigate to https://example.com
  Click button by CSS selector
  Extract page text
  Extract hyperlinks
  ```

- **Semantic Search** (3 tools)
  ```python
  Add documents to search index
  Search for information by meaning
  List all collections
  ```

## Environment Configuration

Edit `.env` to configure:

```bash
# Ollama Models
OLLAMA_PLANNING_MODEL_NAME=ministral-3:latest
OLLAMA_EXECUTION_MODEL_NAME=ministral-3:latest
OLLAMA_PLANNING_TEMPERATURE=0.7
OLLAMA_EXECUTION_TEMPERATURE=0.0

# Backend
# BACKEND_TYPE=composite  # Uncomment for long-term memory
```

## Testing the Agent

Try these prompts to test different features:

1. **Planning**: "Create a research plan for learning Python"
2. **File Operations**: "Create a file called notes.md with today's date"
3. **Web Scraping**: "Scrape https://example.com and tell me the title"
4. **Semantic Search**: "First, add some documents about AI to search index. Then search for 'machine learning'"
5. **Browser**: "Navigate to https://example.com and click the first link"
6. **Subagents**: "Use a subagent to research a specific topic in depth"
7. **Memory** (with --composite): "Save my preferences to /memories/preferences.txt"

## Tips

- **Start Simple**: Use basic mode first to understand agent behavior
- **Enable Composite**: Use `--composite` when you need persistent memory
- **Ask to Plan**: The agent's `write_todos` tool is powerful for complex tasks
- **Use Files**: Agent can save progress to files
- **Be Patient**: First interaction may be slower as model initializes
- **Monitor Logs**: Watch for tool calls and memory operations

## Troubleshooting

**Agent doesn't respond:**
- Check Ollama is running: `ollama ps`
- Verify model is downloaded: `ollama list`
- Check `.env` configuration

**Tools don't work:**
- Check tool is in the 11 tools loaded (logs show this)
- Try invoking tool directly

**Composite backend errors:**
- Ensure `.env` has `BACKEND_TYPE=composite`
- Check routes configuration in logs

## Development

To run with detailed logging:
```bash
LOG_LEVEL=DEBUG uv run python chat.py
```

This will show:
- Tool invocations
- Backend operations
- Memory reads/writes
- Model configurations
