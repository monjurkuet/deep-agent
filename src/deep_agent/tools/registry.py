"""
Helper to register tools with DeepAgents agent.
"""

from deep_agent.tools.scraper import web_scraper_tool
from deep_agent.tools.browser import get_browser_tools


def get_available_tools():
    """Get list of available tools."""
    all_tools = [web_scraper_tool] + get_browser_tools()
    return all_tools
