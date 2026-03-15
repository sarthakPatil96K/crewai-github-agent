import base64
from tools.mcp_client import GitHubClient

client = GitHubClient()


def list_python_files(repo_url):

    data = client.get_tree(repo_url)

    python_files = []

    for file in data.get("tree", []):
        if file["path"].endswith(".py"):
            python_files.append(file["path"])

    return python_files


def read_repo_file(repo_url, file_path):

    file = client.get_file(repo_url, file_path)

    content = base64.b64decode(file["content"]).decode()

    return content