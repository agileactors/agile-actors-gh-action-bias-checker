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


def load_exclude_terms(path=None):
    """
    Load a set of terms to ignore from a JSON file.
    If no path is provided, returns an empty set.

    :param path: str | None: Path to the JSON file containing terms to ignore.
                 Can be set via INPUT_EXCLUDE_TERMS env var.
    :return: set: A set of terms to ignore during bias detection.
    """
    if path is None:
        path = os.environ.get("INPUT_EXCLUDE_TERMS")

    if not path:
        return set()

    if not os.path.exists(path):
        print(f"⚠️ Warning: Exclude terms file '{path}' not found. Ignoring.")
        return set()

    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                return set(data)
            else:
                print(f"⚠️ Warning: Expected a list in {path}. Got {type(data).__name__}. Ignoring.")
                return set()
    except (json.JSONDecodeError, OSError) as e:
        print(f"⚠️ Warning: Failed to load exclude terms from {path}: {e}")
        return set()
