# src/github_api.py

import requests
from typing import Dict, Any, Optional

import logging

logger = logging.getLogger(__name__)


class GitHubAPI:
    def __init__(self, token: str):
        """
        Initialize GitHubAPI with an authentication token.

        :param token: GitHub Personal Access Token for authentication
        """
        self.base_url = "https://api.github.com"
        self.headers = {"Authorization": f"token {token}"}

    def get_repo_diff(
        self, owner: str, repo: str, base: str, head: str
    ) -> Dict[str, Any]:
        """
        Get the diff between two commits (base and head) in a repository.

        :param owner: Owner of the repository
        :param repo: Repository name
        :param base: Base commit SHA or branch name
        :param head: Head commit SHA or branch name
        :return: A dictionary containing the diff data
        """
        url = f"{self.base_url}/repos/{owner}/{repo}/compare/{base}...{head}"
        logging.info(f"Fetching diff data from GitHub API: {url}")
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()

    def get_head_commit(self, owner: str, repo: str, branch: str) -> Any:
        """
        Get the head commit for a specific branch in a repository.

        :param owner: Owner of the repository
        :param repo: Repository name
        :param branch: Branch name
        :return: A dictionary containing the commit data
        """
        url = f"{self.base_url}/repos/{owner}/{repo}/commits/{branch}"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def get_pull_request_diff(
        self, owner: str, repo: str, pr_number: int
    ) -> Optional[str]:
        """
        Get the diff for a specific pull request in a repository.

        :param owner: Owner of the repository
        :param repo: Repository name
        :param pr_number: Pull request number
        :return: A string containing the diff data, or None if not found
        """
        url = f"{self.base_url}/repos/{owner}/{repo}/pulls/{pr_number}"
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            pr_data = response.json()
            return pr_data.get("diff_url")  # Retrieve the diff URL if available
        else:
            return None
