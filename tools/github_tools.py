from crewai.tools import tool
import requests
import base64


def parse_repo_url(repo_url):
    repo_url = repo_url.replace("https://github.com/", "")
    owner, repo = repo_url.split("/")
    return owner, repo


@tool("Get Repository Structure")
def get_repo_structure(repo_url: str) -> str:
    """Returns the files and folders in the root of the repository"""

    owner, repo = parse_repo_url(repo_url)
    api = f"https://api.github.com/repos/{owner}/{repo}/contents"

    response = requests.get(api)

    if response.status_code != 200:
        return "Could not fetch repository."

    data = response.json()

    structure = [item["name"] for item in data]

    return str(structure)


@tool("Read README File")
def get_readme(repo_url: str) -> str:
    """Fetch the README file from the repository"""

    owner, repo = parse_repo_url(repo_url)
    api = f"https://api.github.com/repos/{owner}/{repo}/readme"

    response = requests.get(api)

    if response.status_code != 200:
        return "README not found."

    content = base64.b64decode(response.json()["content"]).decode()

    return content