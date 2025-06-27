# Copyright (c) 2025 Agile Actors
# Licensed under the MIT License. See LICENSE file in the project root for full license information.

import os
import json


def get_scan_patterns():
    """
    Get the file patterns to scan for bias. Defaults to scanning all Python
    files in the repository.
    Returns:
        list: A list of file patterns to scan.
    """
    return os.environ.get("INPUT_SCAN_PATHS", "**/*.py").split(";")


def get_cutoff():
    """
    Get the bias cutoff value from environment variables. Defaults to 0.1 if
    not set.
    :return: float cutoff value
    """
    return float(os.environ.get("INPUT_BIAS_CUTOFF", 0.1))


def load_exclude_terms(path="config/terms_to_ignore.json"):
    """
    Load a set of terms to ignore from a JSON file.
    :param path: str: Path to the JSON file containing terms to ignore.
    :return: set: A set of terms to ignore during bias detection.
    """
    if not os.path.exists(path):
        return set()
    with open(path, "r") as f:
        try:
            return set(json.load(f))
        except json.JSONDecodeError:
            print(f"⚠️ Warning: Failed to decode JSON from {path}. Returning empty set.")
            return set()
