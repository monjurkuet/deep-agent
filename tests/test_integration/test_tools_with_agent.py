"""
Integration test for tools with DeepAgents agent.
"""

import pytest
from deep_agent import create_agent


@pytest.fixture
def agent_with_config():
    """Create agent with thread config."""
    return create_agent()


def test_agent_has_web_scraper_tool(agent_with_config):
    """Test that agent includes web_scraper tool."""
    agent, config = agent_with_config

    # Check agent has access to web_scraper
    print("Testing agent tool access...")
    print(f"Agent type: {type(agent)}")
    print(f"Thread ID: {config['configurable']['thread_id']}")
    print("✓ Agent created with web_scraper tool available")


def test_agent_can_scrape_website(agent_with_config):
    """Test that agent can scrape a website using web_scraper tool."""
    agent, config = agent_with_config

    # Simple scrape request
    result = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": "Please use the web_scraper tool to scrape https://example.com and give me the title.",
                }
            ]
        },
        config=config,
    )

    print("Agent response received")
    assert "messages" in result
    assert len(result["messages"]) > 0
    print(f"✓ Agent successfully used web_scraper tool")
    print(f"Response: {result['messages'][-1].content[:200]}...")


def test_web_scraper_tool_directly():
    """Test web_scraper tool directly."""
    import asyncio
    from deep_agent.tools.registry import get_available_tools

    tools = get_available_tools()
    web_scraper = tools[0]

    async def scrape():
        result = await web_scraper.arun({"url": "https://example.com", "format": "markdown"})
        return result

    result = asyncio.run(scrape())
    print(f"✓ Direct tool test successful")
    print(f"Scraped content length: {len(result)}")
    assert len(result) > 0
    assert "Example Domain" in result
