from dataclasses import dataclass
import glob
from jinja2 import Template
import yaml
import re
import os.path


@dataclass
class Article:
    title: str
    url: str
    date: str
    description: str


class IndexGenerator:
    doc_root: str

    def __init__(self, doc_root: str = "docs"):
        self.doc_root = doc_root

    def parse_article(self, file_path: str) -> Article:
        """
        Parse an article from a file.

        :param file_path: The path to the file containing the article
        :return: An Article object containing the parsed data
        """
        with open(file_path, "r") as file:
            # Extract YAML front matter from the file
            # Read the file content
            content = file.read()

            # Find the start and end of the YAML block
            # marker is line with "---"
            start_match = re.search(r"^---", content, re.MULTILINE)
            end_match = (
                re.search(r"^---", content[start_match.end() :], re.MULTILINE)
                if start_match
                else None
            )

            relative_path = os.path.dirname(file_path.replace(self.doc_root, ""))

            start = start_match.start() if start_match else -1
            end = (
                end_match.start() + start_match.end()
                if start_match and end_match
                else -1
            )

            # Extract the YAML block
            yaml_block = content[start : end + 3]

            # Parse the YAML block into a dictionary
            yaml_data = yaml.safe_load(yaml_block)

            # Extract the required fields from the YAML data
            title = yaml_data.get("title", "")
            url = relative_path + "/index.html"
            description = yaml_data.get("description", "")
            date = yaml_data.get("date", "")

            return Article(title=title, url=url, description=description, date=date)

    def generate_index(self) -> str:
        """
        Generate the index page for the documentation.

        :return: A string containing the generated index page
        """

        articles: list[Article] = []

        # Read the articles from the docs directory using glob
        for file_path in glob.glob(f"{self.doc_root}/*/index.md"):
            # Create an Article object with the extracted data
            article = self.parse_article(file_path)

            # Append the Article object to the articles list
            articles.append(article)

        articles.sort(key=lambda x: x.date, reverse=True)

        # render articles using index.md.j2 template
        with open(f"index.md.j2", "r") as template_file:
            template = Template(template_file.read())
            rendered_index = template.render(articles=articles)

        return rendered_index

    def save_index(self, index: str) -> None:
        """
        Save the generated index page to a file.

        :param index: The generated index page as a string
        """
        with open(f"{self.doc_root}/index.md", "w") as file:
            file.write(index)
