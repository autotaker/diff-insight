from typing import Any, Optional
import yaml
import logging

logger = logging.getLogger(__name__)


class CategoryClassifier:
    """
    Classify patches into categories.
    """

    config: dict[str, Any]

    def __init__(self, config_path):
        """
        Initialize the classifier.

        Args:
            config_path (str): Path to the configuration YAML file.
        """
        with open(config_path) as f:
            self.config = yaml.safe_load(f)

    def classify_patch(self, patch: dict) -> Optional[str]:
        """
        Classifies a patch based on the filename.

        Args:
            patch (dict): The patch to be classified.

        Returns:
            Optional[str]: The category key if the patch is classified, None otherwise.
        """
        filename = patch["filename"]
        for key, category in self.config["categories"].items():
            paths = category["paths"]
            for pattern in paths:
                if filename.startswith(pattern):
                    return key
        logger.warning(f"Could not classify patch: {filename}")
        return None

    def classify_diff(self, diff: dict) -> dict[str, list[dict]]:
        """
        Classifies a diff into categories.

        Args:
            diff (dict): The diff to be classified.

        Returns:
            dict[str, list[dict]]: A dictionary of categories and their corresponding patches.
        """
        classified_diff = {}
        for patch in diff["files"]:
            category = self.classify_patch(patch)
            if category is None:
                continue
            diff_list = classified_diff.get(category, [])
            diff_list.append(patch)
            classified_diff[category] = diff_list
        return classified_diff
