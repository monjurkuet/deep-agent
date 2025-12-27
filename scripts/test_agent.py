"""
Quick test script for manual testing.
"""

import sys

sys.path.insert(0, "../src")

from deep_agent import create_agent
from deep_agent.config.settings import Settings


def main():
    print("=" * 60)
    print("Deep Research Agent - Quick Test")
    print("=" * 60)

    settings = Settings()
    print(f"\nConfiguration:")
    print(f"  Planning Model: {settings.ollama.planning_model}")
    print(f"  Execution Model: {settings.ollama.execution_model}")
    print(f"  Ollama URL: {settings.ollama.base_url}")
    print(f"  Backend Type: {settings.backend.type}")

    try:
        print("\nCreating agent...")
        agent, config = create_agent(settings)
        print("✓ Agent created successfully")

        print("\n" + "=" * 60)
        print("Enter your queries (or 'quit' to exit):")
        print("=" * 60)

        while True:
            query = input("\n> ").strip()

            if query.lower() in ("quit", "exit", "q"):
                print("Goodbye!")
                break

            print("\nProcessing...")
            result = agent.invoke({"messages": [{"role": "user", "content": query}]}, config=config)

            response = result["messages"][-1].content
            print(f"\nAgent: {response}")

    except Exception as e:
        print(f"\n✗ Error: {e}")
        import traceback

        traceback.print_exc()


if __name__ == "__main__":
    main()
