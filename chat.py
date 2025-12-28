"""
Simple interactive chat interface for Deep Agent.
"""

import sys
from deep_agent import create_agent


def main():
    """Run simple chat interface."""

    print("""
╔══════════════════════════════════════════╗
║          Deep Agent - Interactive Chat          ║
╚════════════════════════════════════════╝

Features:
  • 11 tools (web scraper, browser, semantic search)
  • Model configuration via environment
  • Thread persistence with memory
  
Agent features:
  • Planning with write_todos tool
  • Filesystem management
  • Subagent spawning
  
Type your messages below (or 'quit' to exit):
    """)

    agent, config = create_agent()

    print("✅ Agent created successfully")
    print(f"📊 Thread ID: {config['configurable']['thread_id']}")
    print(f"🔧 Model: Using execution model from settings")
    print("\nAgent ready! Type your message below:\n")
    print("=" * 60)

    while True:
        try:
            user_input = input("\n>>> ").strip()

            if not user_input:
                continue

            if user_input.lower() in ("quit", "exit", "q"):
                print("\n👋 Goodbye!")
                break

            print(f"\n{'=' * 60}")
            print(f"👤 User: {user_input}")
            print(f"{'=' * 60}\n")

            result = agent.invoke(
                {"messages": [{"role": "user", "content": user_input}]}, config=config
            )

            response = result["messages"][-1].content
            print(f"🤖 Agent: {response[:500]}")
            if len(response) > 500:
                print(f"{'=' * 60}")
                print(f"   ...({len(response) - 500} more characters)")

            print(f"{'=' * 60}\n")

        except KeyboardInterrupt:
            print("\n\n👋 Interrupted. Goodbye!")
            break
        except EOFError:
            print("\n\n👋 End of input. Goodbye!")
            break
        except Exception as e:
            print(f"\n❌ Error: {e}")


if __name__ == "__main__":
    main()
