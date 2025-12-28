"""
Browser tools using Playwright for web automation.
"""

from langchain_community.agent_toolkits.playwright import PlayWrightBrowserToolkit
from langchain_community.tools.playwright.utils import create_async_playwright_browser
from loguru import logger


def get_browser_tools():
    """Get browser tools (cached, with shared browser context)."""
    global _browser_instance
    global _browser_tools_list
    
    # Return cached tools if already initialized
    if _browser_tools_list is not None:
        try:
            logger.info("Initializing Playwright browser (async)...")
            
            # Create async browser following documentation pattern
            async def _create_browser_context():
                async with create_async_playwright_browser(headless=True) as async_browser:
                    toolkit = PlayWrightBrowserToolkit.from_browser(async_browser=async_browser)
                    return toolkit.get_tools()
            
            # Use nest_asyncio to allow nested event loops
            nest_asyncio.apply()
            tools = asyncio.run(_create_browser_context())
            
            # Store browser instance for tools
            _browser_instance = tools[0]._browser if tools else None
            _browser_tools_list = tools
            
            logger.info(f"Initialized {len(tools)} browser tools (async)")
            return _browser_tools_list
            
        except Exception as e:
            logger.error(f"Failed to initialize browser tools: {e}")
            return []
    except Exception:
        logger.error("Unexpected error during browser initialization")
        return []
