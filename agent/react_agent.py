import os
from langgraph.prebuilt import create_react_agent
from langchain_anthropic import ChatAnthropic
from langchain_core.messages import HumanMessage, SystemMessage
from agent.python_executor_tool import execute_python_code


class PythonExecutorAgent:
    """A ReAct agent that can execute Python code in a sandbox."""
    
    def __init__(self, model_name: str = "claude-sonnet-4-5-20250929", temperature: float = 0):
        """
        Initialize the Python Executor Agent.
        
        Args:
            model_name: The Anthropic model to use
            temperature: The temperature for generation (0 = deterministic)
        """
        self.llm = ChatAnthropic(
            model=model_name,
            temperature=temperature,
            api_key=os.getenv("ANTHROPIC_API_KEY")
        )
        
        self.tools = [execute_python_code]
        
        self.agent = create_react_agent(self.llm, self.tools)
    
    def invoke(self, message: str, system_message: str = None) -> str:
        """
        Invoke the agent with a message.
        
        Args:
            message: The user message
            system_message: Optional system message to guide the agent
            
        Returns:
            str: The agent's final response
        """
        messages = []
        
        if system_message:
            messages.append(SystemMessage(content=system_message))
        
        messages.append(HumanMessage(content=message))
        
        result = self.agent.invoke({"messages": messages})
        
        return result["messages"][-1].content
    
    def stream(self, message: str, system_message: str = None):
        """
        Stream the agent's responses.
        
        Args:
            message: The user message
            system_message: Optional system message to guide the agent
            
        Yields:
            Messages as they are generated
        """
        messages = []
        
        if system_message:
            messages.append(SystemMessage(content=system_message))
        
        messages.append(HumanMessage(content=message))
        
        for chunk in self.agent.stream({"messages": messages}):
            yield chunk

