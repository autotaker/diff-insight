# src/report_generator.py

from datetime import date
from typing import Any, List, Dict


class ReportGenerator:
    def __init__(self):
        """
        Initialize ReportGenerator.
        """
        pass

    def generate_markdown_report(
        self, title: str, date: date, permalink: str, explanation: str
    ) -> str:
        """
        Generate a Markdown report from the diff data and its explanation.

        :param diff_data: A dictionary containing the diff data
        :param explanation: A string containing the explanation of the diff
        :return: A string containing the generated Markdown report
        """

        report_lines = [
            "---",
            f"title: {title}",
            f"date: {date.strftime('%Y-%m-%d')}",
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
        with open(filename, "w") as file:
            file.write(report)
