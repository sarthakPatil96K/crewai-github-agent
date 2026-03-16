import requests
import base64


SUPPORTED_EXTENSIONS = [
    ".py",
    ".java",
    ".js",
    ".jsx",
    ".ts",
    ".tsx",
    ".cpp",
    ".c",
    ".ipynb"
]


def parse_repo_url(repo_url):
    repo_url = repo_url.replace("https://github.com/", "").strip("/")
    owner, repo = repo_url.split("/")
    return owner, repo


def get_repo_tree(owner, repo):
    """
    Try both main and master branches
    """

    branches = ["main", "master"]

    for branch in branches:

        api = f"https://api.github.com/repos/{owner}/{repo}/git/trees/{branch}?recursive=1"

        response = requests.get(api)

        if response.status_code == 200:
            return response.json()

    return None


def list_source_files(repo_url, max_files=20):
    """
    Get source files from repository
    """

    owner, repo = parse_repo_url(repo_url)

    data = get_repo_tree(owner, repo)

    if not data:
        print("⚠ Could not fetch repository tree")
        return []

    source_files = []

    for item in data.get("tree", []):

        path = item.get("path", "")

        if any(path.endswith(ext) for ext in SUPPORTED_EXTENSIONS):
            source_files.append(path)

    print(f"📂 Found {len(source_files)} source files")

    return source_files[:max_files]


def read_repo_file(repo_url, file_path, max_chars=2000):
    """
    Read repository file content safely
    """

    owner, repo = parse_repo_url(repo_url)

    api = f"https://api.github.com/repos/{owner}/{repo}/contents/{file_path}"

    response = requests.get(api)

    if response.status_code != 200:
        return ""

    data = response.json()

    try:
        content = base64.b64decode(data["content"]).decode()
    except Exception:
        return ""

    return content[:max_chars]


def index_repository(repo_url, max_files=5):
    """
    Build repository index for LLM analysis
    """

    files = list_source_files(repo_url, max_files=max_files)

    if not files:
        print("⚠ No source files detected")
        return []

    index = []

    for file in files:

        try:
            content = read_repo_file(repo_url, file)

            if content:
                index.append({
                    "path": file,
                    "content": content
                })

        except Exception:
            continue

    print(f"🧠 Indexed {len(index)} files for analysis")

    return index