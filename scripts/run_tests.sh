#!/bin/bash
set -e

echo "=========================================="
echo "Running Deep Research Agent Tests"
echo "=========================================="

# Get script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

# Run pytest from project root
cd "$PROJECT_ROOT"
uv run pytest -v --tb=short --cov=src/deep_agent --cov-report=term-missing

echo ""
echo "=========================================="
echo "All tests passed!"
echo "=========================================="
