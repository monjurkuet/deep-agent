# Contributing to Deep Agent

Thank you for your interest in contributing to Deep Agent! This document provides guidelines and instructions for contributing.

## Development Setup

### Prerequisites
- Python 3.12 or higher
- [uv](https://github.com/astral-sh/uv) package manager
- Ollama running locally (optional, for LLM features)

### Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd deep-agent
   ```

2. **Install dependencies:**
   ```bash
   uv sync
   ```

3. **Verify installation:**
   ```bash
   uv run python -c "import deep_agent; print('OK')"
   ```

## Code Style

### Linting
We use [ruff](https://github.com/astral-sh/ruff) for linting and formatting:

```bash
# Check code style
uv run ruff check src/

# Auto-fix issues
uv run ruff check --fix src/

# Format code
uv run ruff format src/
```

### Type Hints
All code should include type hints using Python's type annotation system:

```python
from typing import Optional, List

def process_data(data: Optional[List[str]]) -> List[str]:
    """Process data with type hints."""
    if not data:
        return []
    return [item.upper() for item in data]
```

### Code Quality Standards
- Follow PEP 8 style guide
- Use descriptive variable and function names
- Include docstrings for all public functions
- Keep functions focused and small (< 50 lines preferred)

## Testing

### Running Tests

```bash
# Run all tests
uv run pytest tests/

# Run specific test module
uv run pytest tests/test_core/

# Run with coverage
uv run pytest --cov=src/deep_agent --cov-report=html tests/
```

### Test Structure
- Unit tests in `tests/` matching source structure
- Integration tests in `tests/test_integration/`
- Use pytest fixtures in `tests/conftest.py` for shared setup

### Writing Tests
```python
import pytest
from deep_agent import create_agent

def test_agent_creation():
    """Test that agent can be created."""
    agent, config = create_agent()
    assert agent is not None
    assert "thread_id" in config["configurable"]
```

### Test Coverage
- Aim for > 80% coverage
- Write tests for edge cases
- Test both success and error paths

## Pull Request Process

### Before Submitting
1. **Run tests:**
   ```bash
   uv run pytest tests/
   uv run ruff check src/
   ```

2. **Update documentation** if adding/changing features
3. **Add tests** for new functionality
4. **Update CHANGELOG.md** with your changes

### PR Guidelines
- Keep PRs focused and small (one feature per PR)
- Include clear description of changes
- Reference related issues
- Ensure CI checks pass before requesting review
- Respond to reviewer feedback promptly

### PR Template
When submitting a PR, include:
- **Description:** What and why
- **Changes:** Summary of modifications
- **Testing:** How you tested
- **Breaking changes:** If any
- **Related issues:** Links to issues

## Issue Reporting

### Bug Reports
Include:
- Clear description of the bug
- Steps to reproduce
- Expected vs actual behavior
- Environment info (Python version, OS, etc.)
- Error messages/stack traces

### Feature Requests
Include:
- Problem statement
- Proposed solution
- Use cases
- Alternative approaches considered

## Development Workflow

1. **Fork and branch:**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make changes:**
   - Write code
   - Add tests
   - Update docs
   - Run linting and tests

3. **Commit:**
   ```bash
   git add .
   git commit -m "feat: add feature description"
   ```

   Use conventional commits:
   - `feat:` New feature
   - `fix:` Bug fix
   - `docs:` Documentation changes
   - `refactor:` Code refactoring
   - `test:` Test changes

4. **Push and create PR**

## Questions?

Feel free to:
- Open an issue for questions
- Join discussions (when available)
- Contact maintainers directly for complex changes

Thank you for contributing! 🙏
