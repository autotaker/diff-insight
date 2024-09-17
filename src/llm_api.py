# src/llm_api.py

import hashlib
import json
import textwrap
from openai import OpenAI

from typing import Any, Optional
import logging
import locale
import re

logger = logging.getLogger(__name__)

def parse_summary(diff_item: dict[str, Any], explanation: str) -> dict[str, str]:
    """
    Parse the summary from the generated explanation.
    
    :param filename: The filename of the modified file
    :param explanation: The generated explanation
    :return: A dictionary containing the parsed summary

    :Example:
    explanation = '''
    ### Summary

    ```json
    {
        "modification_type": "new feature",
        "modification_title": "Add support for generating diff explanations"
    }
    ```
    '''

    parse_summary(explanation)

        Output: {'modification_type': 'new feature', 'modification_title': 'Add support for generating diff explanations'}
    """
    summary_match = re.search(r"## Summary\n\n```json\n(.*?)\n```", explanation, re.DOTALL)
    summary = {}
    summary['filename'] = diff_item['filename']
    summary['status'] = diff_item['status']
    summary['additions'] = diff_item['additions']
    summary['deletions'] = diff_item['deletions']
    summary['changes'] = diff_item['changes']

    if summary_match:
        summary_json = summary_match.group(1)
        summary.update(json.loads(summary_json))
        return summary
    else:
        return summary

def hash_filename(filename: str) -> str:
    """
    Hash the filename to generate a unique identifier.
    
    :param filename: The filename of the modified file
    :return: A unique identifier for the filename
    
    """

    return "item-" + hashlib.md5(filename.encode()).hexdigest()[:6]

def render_filename_link(filename: str) -> str:
    """
    Render a markdown link for the filename.
    
    :param filename: The filename of the modified file
    :return: A markdown link for the filename
    
    """

    hash = hash_filename(filename)
    logging.debug(f"Hash for {filename}: {hash}")
    return f"[{filename.split('/')[-1]}](#{hash})"

def render_summary_table(summary_table: list[dict[str, Any]]) -> str:
    """
    Render the summary table from the parsed summaries.
    
    :param summary_table: A list of parsed summaries
    :return: A string containing the rendered summary table
    
    """

    table  = "|  Filename  | Type |    Title    | Status | A  | D  | M  |\n"
    table += "|------------|------|-------------|--------|----|----|----|\n"
    keys = ['modification_type', 'modification_title', 'status', 'additions', 'deletions', 'changes']
    for summary in summary_table:
        table += (f"| {render_filename_link(summary['filename'])} | " + 
            ' | '.join(str(summary.get(key, '')) for key in keys) + ' | \n'
        )

    return table


class LLMAPI:
    client: OpenAI

    def __init__(self, api_key: str):
        """
        Initialize LLMAPI with an OpenAI API key.

        :param api_key: OpenAI API key for authentication
        """
        self.client = OpenAI(api_key=api_key)

    def generate_summary(self, explanation: str) -> str:
        """
        Generate a summary from the provided explanation.

        :param explanation: The explanation as a string
        :return: A string containing the generated summary
        """
        style = "summary"
        system = textwrap.dedent(
            f"""\
            You are technical writer. 
            You are multilingual. Your report must be written the language according to user's locale.

            ## Styles
            - Summary: Provide a brief summary of the modification.
            - Overview: Provide an overview of the modification.
            - Detailed: Provide a detailed explanation of the modification.
            """
        )
        loc = locale.getlocale()[0]

        prompt = textwrap.dedent("""\
            Locale: {loc}
            Explain the following report in a {style} manner:
            <document>
            {explanation}
            </document>
            """
            ).format(style=style, explanation=explanation, loc=loc)

        logger.info(f"Generating summary for explanation")
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": prompt},
            ],
            max_tokens=1000,
        )
        summary = response.choices[0].message.content or ""
        usage = response.usage
        logger.info(f"Completed generating summary for explanation. Usage: {usage}")

        return summary

    def generate_diff_explanation_item(
        self, diff_data: dict[str, Any], history: Optional[list[Any]] = None
    ) -> tuple[str, dict[str,str], list[Any]]:
        """
        Generate a natural language explanation for the provided diff data.

        :param diff_data: The diff data as a dictionary
        :return: A string containing the generated explanation
        """
        history = history or []
        loc = locale.getlocale()[0]
        style = "overview"
        system = textwrap.dedent(
            f"""\
            You are technical writer. 
            You are multilingual. Your report must be written the language according to user's locale.

            ## Styles
            - Summary: Provide a brief summary of the modification.
            - Overview: Provide an overview of the modification.
            - Detailed: Provide a detailed explanation of the modification.

            ## Output Format
            Your explanation should be in the following format:
            Do not include `<format>` tags.
            
            <format>
            ### Summary

            ```json
            {{
                "modification_type": "{{purpose of the modification. Candidates are: \
                    'new feature', 'breaking change', 'bug fix', 'minor update'}}",
                "modification_title": "{{Short title of the modification. Locale: {loc} }}"
            }}
            ```

            ### Explanation
            {{explanation}}
            </format>
            """
        )

        prompt = f"Locale: {loc}\n Explain the following code diff in a {style} manner:\n{diff_data}"

        logger.info(
            f"Generating explanation for {diff_data["filename"]}. Style: {style} Locale: {loc}"
        )
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system},
                *history,
                {"role": "user", "content": prompt},
            ],
            max_tokens=1000,
        )
        retry = 0
        while retry < 3:
            try:
                assistant_response = response.choices[0].message.content or ''
                summary = parse_summary(diff_data, assistant_response)
                break
            except json.JSONDecodeError:
                logging.warning("Failed to parse assistant response. Retrying.")
                retry += 1
                continue
        else:
            raise Exception(f"Failed to parse assistant response: {response.choices[0].message.content}")
        
        logging.debug(f"Assistant response: {assistant_response}")
        history.append({"role": "user", "content": prompt})
        history.append({"role": "assistant", "content": assistant_response})
        # Keep only the last 4 interactions in history
        history = history[-4:]
        usage = response.usage
        logger.info(f"Completed generating explanation for diff data. Usage: {usage}")
        logger.info(f"Summary: {summary}")

        return assistant_response, summary, history

    def generate_diff_explanation(
        self, diff_data: list[dict[str, Any]], style: str = "detailed"
    ) -> tuple[str, str]:
        """
        Generate a natural language explanation for the provided diff data.

        :param diff_data: The diff data as a string
        :param style: The style of explanation (e.g., "summary", "detailed")
        :return: A tuple containing the generated explanation and short summary
        """

        explanation = ""
        explanation_report = ""
        history = []
        loc = locale.getlocale()[0]
        summary_table : list[dict[str, str]] = []
        for item in diff_data:
            item_explanation, summary, history = self.generate_diff_explanation_item(
                item, history
            )
            hash = hash_filename(item["filename"])
            logging.debug(f"Hash for {item['filename']}: {hash}")
            explanation += f"### {item['filename']}\n\n" + item_explanation + "\n\n"
            explanation_report += f"## {item['filename']}{{#{hash}}}\n\n"
            if 'patch' in item:
                # find longest fence (^````*) in the patch
                fences = ["```"] + re.findall(r"^(`{3,})", item['patch'], re.MULTILINE)
                longest_fence = max(fences, key=len)
                markdown_fence = longest_fence + '`'

                explanation_report += textwrap.dedent("""\
                    <details>
                    <summary>Diff</summary>
                    {markdown_fence}diff
                    {patch}
                    {markdown_fence}
                    </details>

                    {item_explanation}

                    """).format(patch=item['patch'], item_explanation=item_explanation, markdown_fence=markdown_fence)
            else:
                explanation_report += item_explanation + "\n\n"

            summary_table.append(summary)
        style = "detailed"

        system = textwrap.dedent(
            f"""\
            You are technical writer.

            ## Styles
            - Summary: Provide a brief summary of the modification.
            - Overview: Provide an overview of the modification.
            - Detailed: Provide a detailed explanation of the modification.

            ## Output Format
            Your explanation should be in the following format:
            Do not include `<format>` tags.
            
            <format>
            # Highlights
            {{Summarize the highlights of the diff.
              Forcus on new features and breaking changes.}}

            ## New features

            ## Breaking changes

            ## Other updates

            # Insights
            {{Your insights from the diff. 
              Don't just summarize the diff. 
              User wants to know what changed and why.
              Describe it as a technical article.
            }}
            </format>
            """
        )
        prompt = textwrap.dedent(
            f"""\
            Locale: ${loc}
            Write a report to explain the following code diff in a {style} manner:
            You are multilingual. Your report must be written the language according to user's locale.
            <diff>
            {{explanation}}
            </diff>
            """
        ).format(explanation=explanation)

        logger.info(f"Generating explanation for diff data. Style: {style}")
        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": prompt},
            ],
            max_tokens=1000,
        )
        assistant_response = response.choices[0].message.content or ""
        usage = response.usage
        logging.debug(f"Assistant response: {assistant_response}")
        logging.info(f"Completed generating explanation for diff data. Usage: {usage}")

        summary = self.generate_summary(assistant_response)

        report = textwrap.dedent(
            """
            {assistant_response}

            # Summary Table
            {summary_table}

            # Modified Contents
            {explanation}
            """
        ).format(assistant_response=assistant_response, explanation=explanation_report, summary_table=render_summary_table(summary_table))

        return report, summary
