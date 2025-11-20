import os
from koyeb import Sandbox
import dotenv

dotenv.load_dotenv()


class SandboxTool:
    def __init__(self):
        self.sandbox = None

    @staticmethod
    def get_new_sandbox(image: str = "ubuntu", name: str = "sandbox", wait_ready: bool = True):
        """
        Create a new sandbox environment.
        
        Args:
            image: The base image for the sandbox (default: "ubuntu")
            name: Name for the sandbox (default: "sandbox")
            wait_ready: Wait for sandbox to be ready before returning (default: True)
            
        Returns:
            Sandbox: A new Koyeb sandbox instance
        """
        sandbox = Sandbox.create(
            image=image,
            name=name,
            wait_ready=wait_ready,
        )
        return sandbox
    
    def create_sandbox(self, image: str = "ubuntu", name: str = "sandbox", wait_ready: bool = True):
        """
        Create and store a sandbox instance in this tool.
        
        Args:
            image: The base image for the sandbox (default: "ubuntu")
            name: Name for the sandbox (default: "sandbox")
            wait_ready: Wait for sandbox to be ready before returning (default: True)
            
        Returns:
            Sandbox: The created sandbox instance
        """
        self.sandbox = self.get_new_sandbox(image, name, wait_ready)
        return self.sandbox
    
    def execute_command(self, command: str):
        """
        Execute a command in the current sandbox.
        
        Args:
            command: The command to execute
            
        Returns:
            The execution result
        """
        if not self.sandbox:
            raise RuntimeError("No sandbox available. Create one first using create_sandbox()")
        return self.sandbox.exec(command)
    
    def write_file(self, path: str, content: str):
        """
        Write content to a file in the sandbox.
        
        Args:
            path: The file path in the sandbox
            content: The content to write
        """
        if not self.sandbox:
            raise RuntimeError("No sandbox available. Create one first using create_sandbox()")
        self.sandbox.filesystem.write_file(path, content)
    
    def read_file(self, path: str) -> str:
        """
        Read a file from the sandbox.
        
        Args:
            path: The file path in the sandbox
            
        Returns:
            str: The file content
        """
        if not self.sandbox:
            raise RuntimeError("No sandbox available. Create one first using create_sandbox()")
        return self.sandbox.filesystem.read_file(path)
    
    def delete_sandbox(self):
        """
        Delete the current sandbox.
        """
        if self.sandbox:
            self.sandbox.delete()
            self.sandbox = None
    
    def __enter__(self):
        """Context manager entry."""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit - automatically delete sandbox."""
        self.delete_sandbox()
