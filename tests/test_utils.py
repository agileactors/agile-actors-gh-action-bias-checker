# Copyright (c) 2025 Agile Actors
# Licensed under the MIT License. See LICENSE file in the project root for full license information.

import unittest
from bias_detector.utils import normalize_word

class TestUtils(unittest.TestCase):
    def test_snake_case(self):
        result = normalize_word("user_id")
        self.assertEqual(result, ["user", "id"])

    def test_camel_case_with_digits(self):
        result = normalize_word("UserID2020")
        self.assertEqual(result, ["user", "id"])

    def test_camel_case_without_digits(self):
        result = normalize_word("UserID")
        self.assertEqual(result, ["user", "id"])

    def test_mixed_case_with_digits(self):
        result = normalize_word("userID2020")
        self.assertEqual(result, ["user", "id"])

    def test_no_case_change(self):
        result = normalize_word("user")
        self.assertEqual(result, ["user"])

    def test_empty_string(self):
        result = normalize_word("")
        self.assertEqual(result, [])

    def test_numbers_only(self):
        result = normalize_word("12345")
        self.assertEqual(result, [])

    def test_special_characters(self):
        result = normalize_word("user@id!")
        self.assertEqual(result, ["user", "id"])

    def test_words_with_question_mark(self):
        result = normalize_word("user?ID")
        self.assertEqual(result, ["user", "id"])

    def test_words_with_exclamation_mark(self):
        result = normalize_word("user!ID")
        self.assertEqual(result, ["user", "id"])

    def test_words_with_slash(self):
        result = normalize_word("user/id")
        self.assertEqual(result, ["user", "id"])

    def test_words_with_dot(self):
        result = normalize_word("user.id")
        self.assertEqual(result, ["user", "id"])

if __name__ == "__main__":
    unittest.main()
