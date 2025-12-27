"""
Browser tools using Playwright for web automation.
"""

from langchain_community.agent_toolkits import PlayWrightBrowserToolkit
from langchain_community.tools.playwright.utils import create_sync_playwright_browser
from loguru import logger
import asyncio
import nest_asyncio


# Apply nest_asyncio globally to allow nested event loops
nest_asyncio.apply()


def get_browser_tools():
    """Get browser tools, handling both sync and async contexts."""
    try:
        logger.info("Initializing Playwright browser...")
        sync_browser = create_sync_playwright_browser()
        toolkit = PlayWrightBrowserToolkit.from_browser(sync_browser=sync_browser)
        tools = toolkit.get_tools()
        logger.info(f"Initialized {len(tools)} browser tools")
        return tools
    except Exception as e:
        error_msg = str(e)
        if "asyncio loop" in error_msg or "Async API" in error_msg:
            logger.info("Detected asyncio loop, using async browser...")
            return _get_browser_tools_sync()
        logger.error(f"Failed to initialize browser tools: {e}")
        return []


async def _get_browser_tools_async():
    """Get browser tools from async context."""
    try:
        from langchain_community.tools.playwright.utils import create_async_playwright_browser

        logger.info("Initializing Playwright browser (async)...")

        async def _async_init():
            async with create_async_playwright_browser(headless=True) as async_browser:
                toolkit = PlayWrightBrowserToolkit.from_browser(async_browser=async_browser)
                return toolkit.get_tools()

        tools = await _async_init()
        logger.info(f"Initialized {len(tools)} browser tools (async)")
        return tools
    except Exception as e:
        logger.error(f"Failed to initialize async browser tools: {e}")
        return []


def _get_browser_tools_sync():
    """Get browser tools from async context using asyncio.run."""
    try:
        from langchain_community.tools.playwright.utils import create_async_playwright_browser

        logger.info("Initializing Playwright browser (async in sync wrapper)...")

        async def _async_init():
            async with create_async_playwright_browser(headless=True) as async_browser:
                toolkit = PlayWrightBrowserToolkit.from_browser(async_browser=async_browser)
                return toolkit.get_tools()

        tools = asyncio.run(_async_init())
        logger.info(f"Initialized {len(tools)} browser tools (async)")
        return tools
    except Exception as e:
        logger.error(f"Failed to initialize async browser tools: {e}")
        return []
