# Copyright (c) 2025 Agile Actors
# Licensed under the MIT License. See LICENSE file in the project root for full license information.

import re
import glob
from tqdm import tqdm
from bias_detector.utils import normalize_word
from bias_detector.scoring import bias_score


def get_files_from_patterns(patterns):
    files = set()
    for pattern in patterns:
        files.update(glob.glob(pattern.strip(), recursive=True))
    return sorted(files)


def scan_files(files, exclude_terms, embedding, gender_direction, cutoff):
    flagged = []
    for file in tqdm(files):
        try:
            with open(file, "r", encoding="utf-8", errors="ignore") as f:
                for i, line in enumerate(f):
                    words = re.findall(r"\b\w+\b", line)
                    normalized_words = []
                    for word in words:
                        normalized_words.extend(normalize_word(word))
                    for word in normalized_words:
                        if word in exclude_terms:
                            continue
                        score = bias_score(word, embedding, gender_direction)
                        if score > cutoff:
                            msg = (
                                f"{file}:{i + 1} - {word} "
                                f"(bias score: {score:.2f})"
                            )
                            flagged.append(msg)
        except Exception as e:
            print(f"⚠️ Could not read {file}: {e}")
    return flagged
