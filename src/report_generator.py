# src/report_generator.py

from datetime import date
import os
from typing import Any, List, Dict
import yaml


# Define a custom representer for multi-line strings
def str_presenter(dumper, data):
    if "\n" in data:
        # Use block style for multi-line strings
        return dumper.represent_scalar("tag:yaml.org,2002:str", data, style="|")
    return dumper.represent_scalar("tag:yaml.org,2002:str", data)


# Create a custom Dumper class
class CustomDumper(yaml.SafeDumper):
    pass


# Register the custom representer with the custom Dumper
CustomDumper.add_representer(str, str_presenter)


class ReportGenerator:
    def __init__(self):
        """
        Initialize ReportGenerator.
        """
        pass

    def generate_markdown_report(
        self, title: str, date: date, permalink: str, summary: str, explanation: str
    ) -> str:
        """
        Generate a Markdown report from the diff data and its explanation.

        :param diff_data: A dictionary containing the diff data
        :param explanation: A string containing the explanation of the diff
        :return: A string containing the generated Markdown report
        """

        metadata = {
            "title": title,
            "date": date.strftime("%Y-%m-%d"),
            "permalink": permalink,
            "summary": summary,
        }

        report_lines = [
            "---",
            yaml.dump(
                metadata,
                allow_unicode=True,
                default_flow_style=False,
                Dumper=CustomDumper,
            ),
            "---",
            "",
            f'[View Diff on GitHub]({permalink}){{target="_blank"}}',
            explanation,
        ]
        return "\n".join(report_lines)

    def save_report_to_file(self, report: str, filename: str) -> None:
        """
        Save the generated Markdown report to a file.

        :param report: The generated Markdown report as a string
        :param filename: The filename to save the report to
        """
        if not os.path.exists(os.path.dirname(filename)):
            # Create the directory if it doesn't exist
            os.makedirs(os.path.dirname(filename))

        with open(filename, "w") as file:
            file.write(report)
