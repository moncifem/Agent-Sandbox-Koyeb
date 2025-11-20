from langchain_core.tools import tool
from utility.sandbox_tool import SandboxTool


@tool
async def execute_python_code(code: str) -> str:
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
            
            # Check if Python3 is installed, install if not
            check = sandbox_tool.execute_command("command -v python3")
            if not check.stdout.strip():
                sandbox_tool.execute_command("apt-get update -qq && apt-get install -y -qq python3")
            
            sandbox_tool.write_file("/tmp/script.py", f"#!/usr/bin/env python3\n{code}\n")
            sandbox_tool.execute_command("chmod +x /tmp/script.py")
            result = sandbox_tool.execute_command("/tmp/script.py")
            
            output = result.stdout.strip()
            if result.stderr:
                stderr_clean = result.stderr.strip()
                if stderr_clean and not stderr_clean.startswith("debconf:"):
                    output += f"\nErrors:\n{stderr_clean}"
            
            return output if output else "Code executed successfully with no output."
            
    except Exception as e:
        return f"Error executing code: {str(e)}"
