from crewai.tools import tool
from tools.repo_reader import list_python_files, read_repo_file


@tool
def list_python_files_tool(repo_url: str):
    """List python files in repo"""
    return str(list_python_files(repo_url))


@tool
def read_repo_file_tool(repo_url: str, file_path: str):
    """Read file content"""
    return read_repo_file(repo_url, file_path)