# Copyright (c) 2025 Agile Actors
# Licensed under the MIT License. See LICENSE file in the project root for full license information.

import json
import numpy as np
from bias_detector.embeddings import get_vector


def load_gender_axis(embedding, pair_file="config/gender_pairs.json"):
    """
    Compute the gender direction vector from a list of word pairs.

    Each pair defines a conceptual gender axis (e.g., "man" vs "woman").
    The function calculates the difference vectors for each valid pair
    and returns the average of these vectors, representing the overall
    gender direction in the embedding space.

    :param embedding: Dictionary mapping words to their embedding vectors.
    :param pair_file: Path to a JSON file containing gendered word pairs
                      in the format [["man", "woman"], ...].
    :return: A numpy array representing the gender direction vector.
    :raises ValueError: If no valid word pairs are found.
    """
    with open(pair_file, "r") as f:
        pairs = json.load(f)
    diffs = []
    for a, b in pairs:
        a_vec = get_vector(a, embedding)
        b_vec = get_vector(b, embedding)
        if a_vec is not None and b_vec is not None:
            diffs.append(a_vec - b_vec)
    if not diffs:
        raise ValueError("❌ No valid gender pairs found in the embedding.")
    return np.mean(diffs, axis=0)
