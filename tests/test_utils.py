# Copyright (c) 2025 Agile Actors
# Licensed under the MIT License. See LICENSE file in the project root for full license information.

import unittest
from bias_detector.utils import normalize_word

class TestUtils(unittest.TestCase):
    def test_normalize_word(self):
        test_cases = [
            ("user_id", ["user", "id"]),
            ("UserID2020", ["user", "id"]),
            ("UserID", ["user", "id"]),
            ("user", ["user"]),
            ("", []),
            ("12345", []),
            ("user@id!", ["user", "id"]),
            ("user?ID", ["user", "id"]),
            ("user!ID", ["user", "id"]),
            ("user/id", ["user", "id"]),
            ("user.id", ["user", "id"]),
        ]

        for input_str, expected in test_cases:
            with self.subTest(input=input_str):
                result = normalize_word(input_str)
                self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()