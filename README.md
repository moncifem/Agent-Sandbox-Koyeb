# Python Code Executor Agent with Koyeb Sandbox

A LangGraph ReAct agent powered by Anthropic's Claude that can execute Python code in secure Koyeb sandbox environments.

## Features

- 🤖 **ReAct Agent**: Uses LangGraph's prebuilt ReAct agent with Anthropic Claude
- 🔒 **Secure Execution**: Runs Python code in isolated Koyeb sandbox environments
- 🛠️ **Tool Integration**: Custom LangChain tool for sandbox code execution
- 🌊 **Streaming Support**: Stream agent responses in real-time

## Installation

1. Clone the repository and navigate to the project directory:

```bash
cd koyeb
```

2. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Set up environment variables:

Copy `.env.example` to `.env` and fill in your API keys:

```bash
cp .env.example .env
```

Edit `.env` with your actual API keys:
- Get your Koyeb API token from: https://app.koyeb.com/settings/api
- Get your Anthropic API key from: https://console.anthropic.com/

## Usage

### Basic Example

```python
from agent import PythonExecutorAgent

# Create the agent
agent = PythonExecutorAgent()

# Execute Python code
response = agent.invoke(
    "Execute this Python code: print('Hello, World!')"
)
print(response)
```

### With System Message

```python
response = agent.invoke(
    "Calculate the factorial of 10 using Python",
    system_message="You are a helpful Python coding assistant."
)
print(response)
```

### Streaming Responses

```python
for chunk in agent.stream("Write Python code to generate Fibonacci sequence"):
    print(chunk)
```

### Run the Example

```bash
python main.py
```

## Project Structure

```
koyeb/
├── agent/
│   ├── __init__.py
│   ├── react_agent.py           # LangGraph ReAct agent
│   └── python_executor_tool.py  # LangChain tool for code execution
├── utility/
│   ├── __init__.py
│   └── sandbox_tool.py          # Koyeb sandbox wrapper
├── main.py                       # Example usage
├── requirements.txt              # Python dependencies
├── .env.example                  # Environment variables template
└── README.md                     # This file
```

## How It Works

1. **Agent Creation**: The `PythonExecutorAgent` uses LangGraph's `create_react_agent` to create a ReAct agent with Claude
2. **Tool Binding**: The `execute_python_code` tool is bound to the agent
3. **Sandbox Execution**: When the agent decides to execute code, it:
   - Creates a Koyeb sandbox environment
   - Writes the Python code to a file
   - Executes the code securely
   - Returns the output
   - Cleans up the sandbox automatically

## API Reference

### PythonExecutorAgent

```python
PythonExecutorAgent(
    model_name: str = "claude-3-5-sonnet-20241022",
    temperature: float = 0
)
```

**Methods:**
- `invoke(message: str, system_message: str = None) -> str`: Run the agent and return the response
- `stream(message: str, system_message: str = None)`: Stream agent responses

### execute_python_code Tool

```python
@tool
def execute_python_code(code: str) -> str:
    """Execute Python code in a secure Koyeb sandbox environment."""
```

## Requirements

- Python 3.8+
- Koyeb account (Starter, Pro, or Scale plan)
- Anthropic API key

## License

MIT

