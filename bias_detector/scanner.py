# Copyright (c) 2025 Agile Actors
# Licensed under the MIT License. See LICENSE file in the project root for full license information.

import re
import glob
from functools import lru_cache

from tqdm import tqdm
from bias_detector.utils import normalize_word
from bias_detector.scoring import bias_score


@lru_cache(maxsize=10000)
def cached_normalize_word(word):
    """
    Normalize a word by removing special characters and converting to lowercase.
    This function is cached to improve performance.
    """
    return normalize_word(word)


def get_files_from_patterns(patterns):
    files = set()
    for pattern in patterns:
        files.update(glob.glob(pattern.strip(), recursive=True))
    return sorted(files)


def scan_files(files, exclude_terms, embedding, gender_direction, cutoff):
    flagged = []
    for file in tqdm(files, desc="Scanning files", unit="file"):
        try:
            with open(file, "r", encoding="utf-8", errors="ignore") as f:
                for i, line in enumerate(f):
                    words = re.findall(r"\b\w+\b", line)
                    normalized_words = [
                        nw for word in words for nw in cached_normalize_word(word)
                    ]
                    for word in normalized_words:
                        if not word or word in exclude_terms:
                            continue
                        score = bias_score(word, embedding, gender_direction)
                        if score > cutoff:
                            flagged.append(
                                f"{file}:{i + 1} - {word} (bias score: {score:.2f})"
                            )
        except Exception as e:
            print(f"⚠️ Could not read {file}: {e}")

    return flagged
