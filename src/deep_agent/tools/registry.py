"""
Helper to register tools with DeepAgents agent.
"""

from deep_agent.tools.scraper import web_scraper_tool
from deep_agent.tools.browser import get_browser_tools
from deep_agent.tools.semantic_search import (
    semantic_search,
    add_to_search_index,
    list_search_collections,
)


def get_available_tools():
    """Get list of available tools."""
    all_tools = [web_scraper_tool] + get_browser_tools()
    all_tools += [semantic_search, add_to_search_index, list_search_collections]
    return all_tools
