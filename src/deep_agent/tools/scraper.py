"""
Web scraper tool using Crawl4AI.
"""

import asyncio
from langchain_core.tools import StructuredTool
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, CacheMode
from deep_agent.core.exceptions import ToolError
from loguru import logger
from pydantic import BaseModel, Field


class ScraperInput(BaseModel):
    """Input schema for web scraper tool."""

    url: str = Field(description="URL to scrape")
    format: str = Field(default="markdown", description="Output format ('markdown' or 'text')")


def _scrape_webpage(url: str, format: str = "markdown") -> str:
    """
    Scrape a web page and extract content.

    Args:
        url: URL to scrape
        format: Output format ('markdown' or 'text')

    Returns:
        Extracted content as string
    """
    try:
        logger.info(f"Scraping URL: {url}")

        async def crawl():
            config = CrawlerRunConfig(
                cache_mode=CacheMode.BYPASS,
                word_count_threshold=10,
            )

            async with AsyncWebCrawler() as crawler:
                result = await crawler.arun(url=url, config=config)

                if result.success:
                    if format == "markdown":
                        return result.markdown
                    else:
                        return result.cleaned_html
                else:
                    error_msg = f"Scraping failed: {result.error_message}"
                    logger.error(error_msg)
                    raise ToolError(error_msg)

        return asyncio.run(crawl())

    except ToolError:
        raise
    except Exception as e:
        error_msg = f"Error scraping {url}: {e}"
        logger.error(error_msg)
        raise ToolError(error_msg)


web_scraper_tool = StructuredTool.from_function(
    func=_scrape_webpage,
    name="web_scraper",
    description="Scrape web pages and extract content as markdown or text. Use this for reading articles, documentation, and blog posts.",
    args_schema=ScraperInput,
)
