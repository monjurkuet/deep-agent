# Working with Claude AI Assistant

This guide explains how to efficiently work with this AI assistant for maximum productivity and context management.

## Table of Contents

1. [Context & Memory](#context--memory)
2. [Session Management](#session-management)
3. [Efficient Workflows](#efficient-workflows)
4. [Asking Questions](#asking-questions)
5. [Resuming Work](#resuming-work)
6. [Best Practices](#best-practices)
7. [Quick Reference](#quick-reference)

---

## Context & Memory

### What I Remember
✅ **Within a session:**
- All code you've shown me
- Files I've read/edited
- Previous questions and answers
- Test results and errors

❌ **Across sessions:**
- **Nothing** - context is cleared when you start a new session
- You must provide context each time

### The "Fresh Slate" Rule

**Every new conversation = fresh start.** Even if you say "continue from last session," I won't know what we did.

---

## Session Management

### What Are Sessions?

Each time you start a new conversation with Claude, it's a **new session**.

**Examples of new sessions:**
- Refreshing the Claude webpage
- Starting a new chat in Claude Desktop
- Opening a new AI-assisted IDE window
- After a timeout and re-connecting

### How to Track Sessions

**This project uses session files:**
- `scripts/session-ses_*.md` - Detailed session log
- `SESSION_SUMMARY.md` - High-level accomplishments
- Git commits - Version control checkpoints

---

## Efficient Workflows

### Workflow 1: Quick Questions

```
You: What's the error in this file?
[paste code/error]

Claude: [Analyzes and provides solution]
```

**Key:** One specific question, provide context immediately.

### Workflow 2: Multi-Step Tasks

**Step 1 - Provide context:**
```
You: We're implementing Phase 2 of Deep Agent.
Current status: Phase 1 complete, tests passing.
I want to implement:
1. Crawl4AI scraper tool
2. Playwright browser tool
3. Register tools with agent

Here's the structure:
[paste project structure]
```

**Step 2 - Break into steps:**
```
You: Let's start by creating the Crawl4AI scraper tool.
Please create src/deep_agent/tools/scraper.py with:
- WebScraperTool class extending BaseTool
- Async implementation using crawl4ai
- Proper error handling

Claude: [Creates file]
```

**Step 3 - Verify:**
```
You: Great, now let's test it.
Run the scraper tool tests.

Claude: [Runs tests]
```

**Key:** Provide overview first, then tackle one thing at a time.

### Workflow 3: Debugging

**Best practice:**
```
You: I'm getting this error:

[full error traceback]

Context:
- File: tests/test_core/test_agent.py:42
- What I was trying to do: Create agent with custom config
- Environment: Ollama is running, models are loaded

Can you help fix this?
```

**Avoid:**
```
❌ Bad: "Why is this failing?"
❌ Bad: "It's not working."

```

### Workflow 4: Resuming Work

**Before Resuming: Do These 3 Things**

**1. Check session file:**
```bash
cat scripts/session-ses_49f4.md
```

**2. Check summary:**
```bash
cat SESSION_SUMMARY.md
```

**3. Test current state:**
```bash
./scripts/run_tests.sh
# or
uv run pytest tests/ -v
```

**How to Resume Effectively:**

**Example 1: Clear direction:**
```
You: Resume from Phase 1 implementation.

Here's the current state from SESSION_SUMMARY.md:
[paste relevant section]

I want to start Phase 2: Custom Tools.
Please begin with creating the browser tool.
```

**Example 2: From error:**
```
You: I'm stuck on this error from last session:

[paste error]

This was when testing agent creation in test_agent.py.
The agent was being created with ministral-3:latest model.
Can you help me fix this?
```

**Example 3: From known status:**
```
You: Last session we completed Phase 1 and all tests pass.
Now I want to add ChromaDB integration.

Here's the file structure so far:
[paste tree]

Start by creating a vector_store.py file in src/deep_agent/storage/
```

---

## Asking Questions

### Do: Be Specific ✅

```
✅ Good: "test_agent_creation is failing with 'ImportError: cannot import name AgentFactory'.
The import is in tests/conftest.py:6."

❌ Bad: "Why is this failing?"
```

### Do: Provide Context ✅

```
✅ Good: "In src/deep_agent/storage/composite.py, add error handling for when
the runtime parameter is None. This is needed for testing."

❌ Bad: "Add error handling."
```

### Do: Show What You Tried ✅

```
You: I tried adding try/except but it didn't work:

[paste your attempt]

Claude: I see the issue - you need to catch BackendError, not Exception.
```

### Don't: Assume Context ❌

```
❌ Bad: "Continue implementing the tool layer."

✅ Good: "In Phase 1, we created src/deep_agent/tools/base.py as a placeholder.
Now for Phase 2, I want to implement browser.py.
Create it following the base class pattern."
```

---

## Best Practices

### For New Projects

1. **Start with overview:**
   - What are we building?
   - What tech stack?
   - What's done vs todo?

2. **Create session file:**
   - I'll automatically save progress
   - Check it to see what we did

3. **Use version control:**
   - Commit after major features
   - Commit messages describe what was done

### For Debugging

1. **Show** error: Full stack trace
2. **Show** code: File path + line numbers
3. **Explain** what you tried: "I tried X but got Y"
4. **Context**: Environment, models, what you were doing

### For Large Tasks

1. **Break into phases:**
   - Phase 1: Setup
   - Phase 2: Core features
   - Phase 3: Advanced features

2. **Tackle one thing at a time:**
   - "Let's start with the configuration"
   - "Good, now let's implement the core agent"

3. **After each phase:**
   - Run tests
   - Update SESSION_SUMMARY.md
   - Commit to git

---

## Quick Reference

### Resume Templates

**From scratch:**
```
I'm starting work on [project name].
[context about project]
Let's begin with [first task].
```

**From session:**
```
You: Resume from [session name/phase].

Here's the summary from last session:
[paste SESSION_SUMMARY.md relevant part]

I want to continue with [next task].
```

**From error:**
```
You: I'm stuck on this error:
[paste error]

Context: [what you were doing]
Can you help fix it?
```

### Context Checklist

Before asking, ensure you provide:
- [ ] What are you trying to do?
- [ ] What have you tried?
- [ ] What's the current error/output?
- [ ] Relevant code/files?

### Efficiency Tips

✅ **DO:**
- Paste code/errors directly
- Provide file paths
- Explain what you want in one message
- Use code blocks for code
- Reference previous work

❌ **DON'T:**
- Make me guess the context
- Spread one question across multiple messages
- Say "continue" without context
- Assume I know your project history

---

## Troubleshooting

### "Claude doesn't remember what we did"

**Cause:** New session started

**Solution:**
```bash
# Check what we accomplished
cat SESSION_SUMMARY.md
cat scripts/session-ses_*.md

# Tell me about it
You: "Resume from Phase 1. We completed [list items].
Now I want to start Phase 2: Custom Tools. Begin with browser tool."
```

### "Claude keeps asking for context"

**Cause:** Not enough information provided

**Solution:**
```
# Instead of:
"Fix the error"

# Use:
"I'm getting ImportError: cannot import name X.
File: tests/conftest.py:6
Context: Trying to import AgentFactory from core.agent"
```

---

## Phase 2: Custom Tools Implementation

### Overview

Phase 2 adds web automation capabilities to the Deep Research Agent:
- **Crawl4AI**: Fast content extraction for research
- **Playwright**: Full browser automation for complex interactions

### Tools Created

#### 2.1: Crawl4AI Scraper (`WebScraperTool`)
- **Purpose**: Extract content from web pages quickly
- **Features**:
  - Async implementation using `crawl4ai.AsyncWebCrawler`
  - Returns markdown or text format
  - Proper error handling with `ToolError`
  - Supports multiple URLs (via crawl4ai.arun_many)

- **File**: `src/deep_agent/tools/scraper.py`

- **Usage Example**:
  ```python
  from deep_agent.tools.scraper import WebScraperTool

  scraper = WebScraperTool()
  result = await scraper("https://example.com", format="markdown")
  print(result)
  ```

- **Best For**: Articles, docs, blog posts
- **Limitations**: No form filling, login flows

#### 2.2: Playwright Browser Tools (7 tools)
- **Purpose**: Full browser automation and interaction
- **Features**:
  - Uses LangChain's `PlaywrightBrowserToolkit`
  - Automatic sync/async context detection (via nest_asyncio)
  - Tools: navigate_browser, click_element, extract_text, extract_hyperlinks, get_elements, current_webpage, previous_webpage

- **File**: `src/deep_agent/tools/browser.py`

- **Usage Example**:
  ```python
  from deep_agent.tools.browser import get_browser_tools
  from deep_agent.tools.registry import get_available_tools

  # Get all tools (includes browser tools)
  tools = get_available_tools()

  # Use navigate tool
  nav_tool = next((t for t in tools if t.name == 'navigate_browser'), None)
  result = nav_tool.invoke({'url': 'https://example.com'})
  print(result)

  # Use extract_text tool
  extract_tool = next((t for t in tools if t.name == 'extract_text'), None)
  result = extract_tool.invoke({})
  print(result[:200])
  ```

- **Available Tools**:
  - `navigate_browser` - Navigate to URLs
  - `click_element` - Click elements by CSS selector
  - `extract_text` - Extract all text from current page
  - `extract_hyperlinks` - Extract hyperlinks from page
  - `get_elements` - Select elements by CSS selector
  - `current_webpage` - Get current page URL
  - `previous_webpage` - Navigate back to previous page

- **Best For**: Forms, logins, complex SPAs, multi-step flows
- **Limitations**: Slower than Crawl4AI, more complex setup
- **Async Handling**: Automatically detects asyncio loops and switches to async browser

### Integration with Agent

**Status**: ✅ Complete

Tools are now automatically registered with DeepAgents agent when created.

**Usage**:
```python
from deep_agent import create_agent

# Agent automatically loads all tools from registry
agent, config = create_agent()

# Tools available to agent: web_scraper + 7 browser tools
```

**Tools Loaded** (8 total):
1. `web_scraper` - Crawl4AI web scraper
2. `navigate_browser` - Navigate to URLs
3. `click_element` - Click elements by selector
4. `extract_text` - Extract page text
5. `extract_hyperlinks` - Extract links
6. `get_elements` - Get elements by selector
7. `current_webpage` - Get current page URL
8. `previous_webpage` - Navigate back

### Design Decisions

1. **Separation**: Each tool in separate file for modularity
2. **Async support**: Both tools use async/await for better performance
3. **Error handling**: Custom `ToolError` for clear error messages
4. **Context management**: Browser tool has async context manager for cleanup

### Next Steps for Phase 2

- [x] 2.6: Register tools with DeepAgents agent configuration ✅
- [x] 2.7: Integration tests (use tools with agent) ✅
- [x] 2.8: Browser tools async/sync fix ✅
- [x] 2.9: Documentation updates (SESSION_SUMMARY.md) ✅
- [x] 2.10: Documentation updates (WORKING_WITH_AI.md) ✅

**Phase 2 Status: COMPLETE ✅**

---

## Summary

**Golden Rule:** Always provide context when starting a new session.

**Remember:**
- Each chat = new session
- I don't have cross-session memory
- You need to tell me what you're working on

**Best workflow:**
1. Check SESSION_SUMMARY.md
2. Tell me what to work on
3. Let me complete the task
4. Review and move to next

---

**Need Help?** Just paste this:
```
"I need help. Context: [describe your situation].
What I tried: [what you did].
The issue: [error/problem]."
```
