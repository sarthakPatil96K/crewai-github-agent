import requests


class GitHubClient:

    BASE = "https://api.github.com"

    def parse_repo(self, repo_url):
        repo_url = repo_url.replace("https://github.com/", "")
        owner, repo = repo_url.split("/")
        return owner, repo

    def get_tree(self, repo_url):
        owner, repo = self.parse_repo(repo_url)

        url = f"{self.BASE}/repos/{owner}/{repo}/git/trees/main?recursive=1"

        return requests.get(url).json()

    def get_file(self, repo_url, path):
        owner, repo = self.parse_repo(repo_url)

        url = f"{self.BASE}/repos/{owner}/{repo}/contents/{path}"

        return requests.get(url).json()