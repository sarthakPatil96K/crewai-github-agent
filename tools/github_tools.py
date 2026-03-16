from crewai.tools import tool
import requests
import base64
from tools.repo_indexer import index_repository
from tools.repo_reader import list_source_files, read_repo_file


def parse_repo_url(repo_url):
    repo_url = repo_url.replace("https://github.com/", "")
    owner, repo = repo_url.split("/")
    return owner, repo


# -----------------------------
# Repo Structure Tool
# -----------------------------

@tool
def get_repo_structure(repo_url: str):
    """Returns root files and folders of the repository"""

    owner, repo = parse_repo_url(repo_url)

    api = f"https://api.github.com/repos/{owner}/{repo}/contents"

    response = requests.get(api)

    if response.status_code != 200:
        return "Could not fetch repository structure."

    data = response.json()

    structure = [item["name"] for item in data]

    return str(structure)


# -----------------------------
# README Tool
# -----------------------------

@tool
def get_readme(repo_url: str):
    """Fetch repository README"""

    owner, repo = parse_repo_url(repo_url)

    api = f"https://api.github.com/repos/{owner}/{repo}/readme"

    response = requests.get(api)

    if response.status_code != 200:
        return "README not found."

    content = base64.b64decode(response.json()["content"]).decode()

    return content


# -----------------------------
# Python File Scanner
# -----------------------------

@tool
def list_python_files_tool(repo_url: str):
    """List python files in repo"""

    return str(list_source_files(repo_url))


# -----------------------------
# File Reader
# -----------------------------

@tool
def read_repo_file_tool(repo_url: str, file_path: str):
    """Read file content"""

    return read_repo_file(repo_url, file_path)





@tool
def index_repository_tool(repo_url: str):
    """Return indexed repository files (limited for token safety)"""
    return index_repository(repo_url)