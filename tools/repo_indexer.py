from tools.repo_reader import list_source_files, read_repo_file


def index_repository(repo_url):
    """
    Build an index of python files and their contents
    """

    files = list_source_files(repo_url)

    repo_index = []

    for file in files:

        content = read_repo_file(repo_url, file)

        if "Could not" in content:
            continue

        repo_index.append({
            "path": file,
            "content": content[:5000]  # limit tokens
        })

    return repo_index