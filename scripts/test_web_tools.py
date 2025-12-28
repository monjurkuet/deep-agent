#!/usr/bin/env python
"""
Test web automation tools one by one.

This script tests:
1. web_scraper - Crawl4AI web scraper
2. navigate_browser - Navigate to URLs
3. click_element - Click elements by CSS selector
4. extract_text - Extract page text
5. extract_hyperlinks - Extract links
6. get_elements - Get elements by selector
7. current_webpage - Get current page URL
8. previous_webpage - Navigate back
"""

import asyncio
from deep_agent.tools.scraper import web_scraper_tool
from deep_agent.tools.browser import get_browser_tools
from loguru import logger


def test_web_scraper():
    """Test 1: web_scraper tool."""
    print("\n" + "=" * 60)
    print("TEST 1: web_scraper (Crawl4AI)")
    print("=" * 60)

    try:
        print("\n[1/2] Testing with markdown format...")
        result = web_scraper_tool.invoke({"url": "https://example.com", "format": "markdown"})
        print(f"✓ Markdown scraping successful")
        print(f"  Content length: {len(result)} characters")
        print(f"  First 200 chars: {result[:200]}...")
        assert "Example Domain" in result
        print("✓ Content validation passed")

        print("\n[2/2] Testing with text format...")
        result = web_scraper_tool.invoke({"url": "https://example.com", "format": "text"})
        print(f"✓ Text scraping successful")
        print(f"  Content length: {len(result)} characters")

        print("\n✅ web_scraper: ALL TESTS PASSED\n")
        return True

    except Exception as e:
        print(f"\n❌ web_scraper: FAILED - {e}\n")
        return False


def test_browser_tools():
    """Test Playwright browser tools."""
    print("\n" + "=" * 60)
    print("TEST 2-8: Playwright Browser Tools")
    print("=" * 60)

    try:
        # Get all browser tools
        tools = get_browser_tools()
        print(f"\n✓ Initialized {len(tools)} browser tools")

        # Map tool names for easy access
        tool_map = {t.name: t for t in tools}

        print("\nAvailable tools:")
        for i, tool in enumerate(tools, 1):
            print(f"  {i}. {tool.name}")

        # Test 2: navigate_browser
        print("\n" + "-" * 60)
        print("TEST 2: navigate_browser")
        print("-" * 60)
        nav_tool = tool_map.get("navigate_browser")
        if nav_tool:
            result = nav_tool.invoke({"url": "https://example.com"})
            print(f"✓ Navigate successful")
            print(f"  Result: {result[:200]}")
        else:
            print("❌ navigate_browser tool not found")
            return False

        # Test 3: current_webpage
        print("\n" + "-" * 60)
        print("TEST 3: current_webpage")
        print("-" * 60)
        url_tool = tool_map.get("current_webpage")
        if url_tool:
            result = url_tool.invoke({})
            print(f"✓ Current URL: {result}")
            assert "example.com" in result
            print("✓ URL validation passed")
        else:
            print("❌ current_webpage tool not found")
            return False

        # Test 4: extract_text
        print("\n" + "-" * 60)
        print("TEST 4: extract_text")
        print("-" * 60)
        extract_tool = tool_map.get("extract_text")
        if extract_tool:
            result = extract_tool.invoke({})
            print(f"✓ Text extraction successful")
            print(f"  Extracted {len(result)} characters")
            print(f"  First 200 chars: {result[:200]}...")
            assert "Example Domain" in result
            print("✓ Content validation passed")
        else:
            print("❌ extract_text tool not found")
            return False

        # Test 5: extract_hyperlinks
        print("\n" + "-" * 60)
        print("TEST 5: extract_hyperlinks")
        print("-" * 60)
        links_tool = tool_map.get("extract_hyperlinks")
        if links_tool:
            result = links_tool.invoke({})
            print(f"✓ Hyperlinks extraction successful")
            print(f"  Found {len(result)} hyperlinks")
            print(f"  Sample links: {result[:3] if len(result) >= 3 else result}")
            assert len(result) > 0
            print("✓ Links validation passed")
        else:
            print("❌ extract_hyperlinks tool not found")
            return False

        # Test 6: get_elements
        print("\n" + "-" * 60)
        print("TEST 6: get_elements")
        print("-" * 60)
        elements_tool = tool_map.get("get_elements")
        if elements_tool:
            result = elements_tool.invoke({"selector": "h1", "attributes": ["innerText"]})
            print(f"✓ Element selection successful")
            print(f"  Found elements: {result}")
            assert len(result) > 0
            print("✓ Elements validation passed")
        else:
            print("❌ get_elements tool not found")
            return False

        # Test 7: navigate to Wikipedia
        print("\n" + "-" * 60)
        print("TEST 7: Navigate to different page")
        print("-" * 60)
        result = nav_tool.invoke({"url": "https://www.wikipedia.org/"})
        print(f"✓ Navigate to Wikipedia successful")
        print(f"  Result: {result[:200]}")

        # Verify current page changed
        current_url = url_tool.invoke({})
        print(f"  Current URL: {current_url}")
        assert "wikipedia.org" in current_url
        print("✓ Page change verification passed")

        # Test 8: previous_webpage
        print("\n" + "-" * 60)
        print("TEST 8: previous_webpage")
        print("-" * 60)
        prev_tool = tool_map.get("previous_webpage")
        if prev_tool:
            result = prev_tool.invoke({})
            print(f"✓ Navigate back successful")
            print(f"  Result: {result[:200]}")

            # Verify we're back on example.com
            current_url = url_tool.invoke({})
            print(f"  Current URL: {current_url}")
            assert "example.com" in current_url
            print("✓ Back navigation verification passed")
        else:
            print("❌ previous_webpage tool not found")
            return False

        # Test 9: click_element (if clickable element exists)
        print("\n" + "-" * 60)
        print("TEST 9: click_element")
        print("-" * 60)
        click_tool = tool_map.get("click_element")
        if click_tool:
            # Try clicking on a link (if available on example.com)
            result = click_tool.invoke({"selector": "a", "element_num": 0})
            print(f"✓ Click operation successful")
            print(f"  Result: {result[:200]}")
        else:
            print("❌ click_element tool not found")
            return False

        print("\n✅ Browser Tools: ALL TESTS PASSED\n")
        return True

    except Exception as e:
        print(f"\n❌ Browser Tools: FAILED - {e}\n")
        import traceback

        traceback.print_exc()
        return False


def main():
    """Run all tests."""
    print("\n" + "=" * 60)
    print("WEB AUTOMATION TOOLS TEST SUITE")
    print("=" * 60)

    results = []

    # Test web_scraper
    results.append(("web_scraper", test_web_scraper()))

    # Test browser tools
    results.append(("browser_tools", test_browser_tools()))

    # Summary
    print("\n" + "=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)

    for name, passed in results:
        status = "✅ PASSED" if passed else "❌ FAILED"
        print(f"{name:20s} {status}")

    total_passed = sum(1 for _, p in results if p)
    total_tests = len(results)

    print(f"\nTotal: {total_passed}/{total_tests} test suites passed")

    if total_passed == total_tests:
        print("\n🎉 ALL TESTS PASSED! 🎉\n")
        return 0
    else:
        print("\n⚠️  SOME TESTS FAILED\n")
        return 1


if __name__ == "__main__":
    exit(main())
