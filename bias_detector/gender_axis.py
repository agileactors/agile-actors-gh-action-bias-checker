import json
import numpy as np
from bias_detector.embeddings import get_vector


def load_gender_axis(embedding, pair_file="config/gender_pairs.json"):
    """
    Computes a gender direction vector from word embeddings
    :param embedding: The word embedding model.
    :param pair_file: Path to the JSON file containing the word pairs.
    :return: It returns the mean of all the difference vectors. This
    resulting vector is the "gender direction" —a general vector
    pointing from female-like words to male-like words in
    embedding space.
    """
    with open(pair_file, "r") as f:
        pairs = json.load(f)
    diffs = [
        get_vector(a, embedding) - get_vector(b, embedding)
        for a, b in pairs
        if (
                get_vector(a, embedding) is not None and
                get_vector(b, embedding) is not None
        )
    ]
    if not diffs:
        raise ValueError("❌ No valid gender pairs found in the embedding.")
    return np.mean(diffs, axis=0)
