# Copyright (c) 2025 Agile Actors
# Licensed under the MIT License. See LICENSE file in the project root for full license information.

import numpy as np
from bias_detector.embeddings import get_vector


def cosine(u, v):
    """
    Calculate the cosine similarity between two vectors.
    :param u: First vector.
    :param v: Second vector.
    :return: Cosine similarity value.
    """
    return np.dot(u, v) / (np.linalg.norm(u) * np.linalg.norm(v))


def bias_score(word, embedding, gender_direction):
    """
    Calculate the bias score of a word based on its vector representation
    :param word: The word to evaluate.
    :param embedding: The word embedding
    :param gender_direction:
    """
    vec = get_vector(word, embedding)
    if vec is None:
        return 0.0
    return abs(cosine(vec, gender_direction))
