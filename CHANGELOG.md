# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0] - 2025-12-28

### Added
- Phase 1: Core agent infrastructure
  - Pydantic-based configuration system with environment loading
  - DeepAgents framework integration with Ollama model support
  - StateBackend for ephemeral filesystem management
  - ChromaDB backend for semantic search
  - Custom exception hierarchy for error handling
  - Loguru-based logging with structured output
  - Comprehensive test suite with pytest
  - AgentFactory for creating configured Deep Agents
  - MemorySaver checkpointer for conversation persistence

 - Phase 2: Web automation tools
   - Crawl4AI web scraper tool (web_scraper)
     - Fast content extraction from web pages
     - Markdown and text output formats
     - Async implementation with proper error handling
   - Playwright browser toolkit (7 tools)
     - navigate_browser - Navigate to URLs
     - click_element - Click elements by CSS selector
     - extract_text - Extract page text
     - extract_hyperlinks - Extract hyperlinks
     - get_elements - Get elements by selector
     - current_webpage - Get current page URL
     - previous_webpage - Navigate back
   - Semantic search tool (3 functions)
     - semantic_search - Search documents by meaning
     - add_to_search_index - Add documents to index
     - list_search_collections - List all collections
     - Ollama embeddings integration (nomic-embed-text)
   - Tool registry system for centralized tool management
   - Automatic tool loading on agent creation
   - Integration tests for all tools
   - Async/sync compatibility for browser tools

- Phase 3: Long-term memory
   - Composite backend with path routing
     - Routes `/memories/` to persistent StoreBackend
     - Routes other paths to ephemeral StateBackend
     - Cross-thread persistence for memory
   - LangGraph Store integration with InMemoryStore
   - Hybrid storage: ephemeral working space + persistent memory
   - Updated Settings with routes configuration
   - 4 new tests for composite backend functionality

### Changed
- Updated agent factory to integrate custom tools automatically
- Added tool logging on agent creation

### Fixed
- Browser tools async/sync compatibility using nest_asyncio
- Proper event loop handling in pytest contexts

## [0.0.1] - Initial Development

### Added
- Project structure setup
- Initial configuration management
- Basic agent scaffolding
