# Copyright (c) 2025 Agile Actors
# Licensed under the MIT License. See LICENSE file in the project root for full license information.

import unittest
from bias_detector.embeddings import get_vector,load_embeddings

class TestEmbeddings(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.embedding = load_embeddings()

    def test_known_word(self):
        word = "king"
        vector = get_vector(word, self.embedding)
        self.assertIsNotNone(vector, f"Vector for '{word}' should not be None")
        self.assertEqual(len(vector), 300, f"Vector for '{word}' should have 300 dimensions")

    def test_unknown_word(self):
        word = "nonexistentword"
        vector = get_vector(word, self.embedding)
        self.assertIsNone(vector, f"Vector for '{word}' should be None")

if __name__ == "__main__":
    unittest.main()