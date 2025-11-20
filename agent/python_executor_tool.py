from langchain_core.tools import tool
from utility.sandbox_tool import SandboxTool


@tool
def execute_python_code(code: str) -> str:
    """
    Execute Python code in a secure Koyeb sandbox environment.
    
    Args:
        code: The Python code to execute
        
    Returns:
        str: The output from executing the code (stdout and stderr)
    """
    try:
        with SandboxTool() as sandbox_tool:
            sandbox_tool.create_sandbox(image="ubuntu", name="python-executor", wait_ready=True)

            sandbox_tool.write_file("/tmp/script.py", f"#!/usr/bin/env python3\n{code}\n")
            
            sandbox_tool.execute_command("chmod +x /tmp/script.py")
            
            result = sandbox_tool.execute_command("python3 /tmp/script.py")
            
            output = result.stdout.strip()
            if result.stderr:
                output += f"\nErrors:\n{result.stderr.strip()}"
            
            return output if output else "Code executed successfully with no output."
            
    except Exception as e:
        return f"Error executing code: {str(e)}"

