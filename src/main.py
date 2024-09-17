# src/main.py

from datetime import datetime
import hashlib
import json
import os
import typer
from cache import Cache
from category_classifier import CategoryClassifier
from github_api import GitHubAPI
from index_generator import IndexGenerator
from llm_api import LLMAPI
from report_generator import ReportGenerator
import logging

app = typer.Typer()

token = os.getenv("GITHUB_TOKEN")
api_key = os.getenv("OPENAI_API_KEY")


@app.command()
def fetch(owner: str, repo: str, base: str, head: str):
    """
    Fetch diff from a GitHub repository between two commits or branches.

    :param owner: Owner of the repository
    :param repo: Repository name
    :param base: Base commit SHA or branch name
    :param head: Head commit SHA or branch name
    """
    if not token:
        typer.echo("Error: GitHub token not found.")
        raise typer.Abort()
    github_api = GitHubAPI(token)
    diff_data = github_api.get_repo_diff(owner, repo, base, head)
    typer.echo(json.dumps(diff_data, ensure_ascii=False, indent=2))


@app.command()
def fetch_commit(owner: str, repo: str, branch: str, output: str):
    """
    Fetch the head commit for a specific branch in a GitHub repository.

    :param owner: Owner of the repository
    :param repo: Repository name
    :param branch: Branch name
    :param output: Output filename for the commit data
    """
    if not token:
        typer.echo("Error: GitHub token not found.")
        raise typer.Abort()
    github_api = GitHubAPI(token)
    commit_data = github_api.get_head_commit(owner, repo, branch)

    with open(output, "w") as file:
        json.dump(commit_data, file)
    typer.echo(f"Commit data saved to {output}")


@app.command()
def generate_report(owner: str, repo: str, base: str, head: str, output: str):
    """
    Fetch diff, generate explanation, and save a Markdown report.

    :param owner: Owner of the repository
    :param repo: Repository name
    :param base: Base commit SHA or branch name
    :param head: Head commit SHA or branch name
    :param output: Output filename for the Markdown report like "report_{date}_{category}.md"
    """
    cache = Cache()
    if not token:
        typer.echo("Error: GitHub token not found.")
        raise typer.Abort()
    if not api_key:
        typer.echo("Error: OpenAI API key not found.")
        raise typer.Abort()
    github_api = GitHubAPI(token)
    base_key = f"{owner}/{repo}/{base}...{head}"
    base_key = hashlib.md5(base_key.encode()).hexdigest()
    diff_data = cache.with_cache(
        f"{base_key}_diff", github_api.get_repo_diff, owner, repo, base, head
    )

    classifier = CategoryClassifier("categories.yaml")

    permalink = diff_data.get("permalink_url", "")

    categories = classifier.classify_diff(diff_data)
    llm_api = LLMAPI(api_key)
    report_generator = ReportGenerator()
    date = datetime.today().date()
    datestr = date.strftime("%Y%m%d")

    if not categories:
        typer.echo("No patches maching the categories.")
        return

    for category, patches in categories.items():
        typer.echo(f"Category: {category}")

        explanation, summary = cache.with_cache(
            f"{base_key}_{category}_explanation",
            llm_api.generate_diff_explanation,
            patches,
            "detailed",
        )

        title = f"Diff Insight Report - {category}"
        report = report_generator.generate_markdown_report(
            title, date, permalink, summary, explanation
        )
        output_path = output.format(category=category, date=datestr)
        report_generator.save_report_to_file(report, output_path)
        typer.echo(f"Report saved to {output_path}")


@app.command()
def generate_index(doc_root: str):
    """
    Generate an index page for the documentation.

    :param doc_root: Root directory of the documentation
    """
    cache = Cache()
    cache_dir = "cache"
    cache.cache_dir = cache_dir

    index_generator = IndexGenerator(doc_root)

    index_page = index_generator.generate_index()

    index_generator.save_index(index_page)
    typer.echo(f"Index page saved to {doc_root}/index.md")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    app()
