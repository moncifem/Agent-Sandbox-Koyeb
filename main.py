"""Example usage of the Python Executor Agent."""
import asyncio
from agent import PythonExecutorAgent


async def main():
    # Make sure you have set KOYEB_API_TOKEN and ANTHROPIC_API_KEY in .env file
    
    agent = PythonExecutorAgent(
        model_name="claude-sonnet-4-5-20250929",
        temperature=0.1
    )
    
    print("Example 1: Simple Python code execution")
    print("-" * 50)
    response = await agent.ainvoke(
        "Execute this Python code: print('Hello from Koyeb Sandbox!')"
    )
    print(f"Agent Response: {response}\n")
    
    print("Example 2: Math calculation")
    print("-" * 50)
    response = await agent.ainvoke(
        "Calculate the factorial of 10 using Python code"
    )
    print(f"Agent Response: {response}\n")
    
    print("Example 3: With custom system message")
    print("-" * 50)
    response = await agent.ainvoke(
        "Write and execute Python code to generate the Fibonacci sequence up to the 10th term",
        system_message="You are a helpful Python coding assistant. Always write clean, well-commented code."
    )
    print(f"Agent Response: {response}\n")


if __name__ == "__main__":
    asyncio.run(main())
