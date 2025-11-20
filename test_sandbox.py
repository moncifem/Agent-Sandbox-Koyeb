from agent.python_executor_tool import execute_python_code
import asyncio
import dotenv

dotenv.load_dotenv()


async def main():
    code = """
import math

result = math.factorial(10)
print(f"Factorial of 10 is: {result}")
"""
    
    result = await execute_python_code.ainvoke(code)
    print("Output:", result)


if __name__ == "__main__":
    asyncio.run(main())