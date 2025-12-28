"""
Browser tools using Playwright for web automation.
"""

from langchain_community.agent_toolkits.playwright import PlayWrightBrowserToolkit
from langchain_community.tools.playwright.utils import create_async_playwright_browser
from loguru import logger


def get_browser_tools():
    """Get browser tools using async initialization pattern from documentation."""
    try:
        logger.info("Initializing Playwright browser (async)...")

        # Create async browser following documentation pattern
        async def _create_browser_tools():
            async with create_async_playwright_browser(headless=True) as async_browser:
                toolkit = PlayWrightBrowserToolkit.from_browser(async_browser=async_browser)
                return toolkit.get_tools()

        import asyncio
        import nest_asyncio

        # Use nest_asyncio to allow nested event loops
        nest_asyncio.apply()
        tools = asyncio.run(_create_browser_tools())

        logger.info(f"Initialized {len(tools)} browser tools (async)")
        return tools
    except Exception as e:
        logger.error(f"Failed to initialize browser tools: {e}")
        return []
