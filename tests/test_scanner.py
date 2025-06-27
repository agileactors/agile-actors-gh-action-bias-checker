# Copyright (c) 2025 Agile Actors
# Licensed under the MIT License. See LICENSE file in the project root for full license information.

import unittest
import tempfile
import os
from unittest.mock import patch
from bias_detector.scanner import scan_files, get_files_from_patterns


class TestScanner(unittest.TestCase):

    def setUp(self):
        self.test_file = tempfile.NamedTemporaryFile(mode="w+", delete=False, suffix=".py")
        self.test_file.write("king queen nurse engineer\n")
        self.test_file.close()

        self.embedding = {
            "king": [1.0, 0.0],
            "queen": [-1.0, 0.0],
            "nurse": [0.5, 0.0],
            "engineer": [-0.5, 0.0]
        }

        self.gender_direction = [1.0, 0.0]

    def tearDown(self):
        os.unlink(self.test_file.name)

    @patch("bias_detector.scanner.normalize_word", side_effect=lambda w: [w])
    @patch("bias_detector.scanner.bias_score")
    def test_scan_files_detects_bias(self, mock_bias_score, _):

        mock_bias_score.side_effect = lambda word, e, gd: 0.6 if word in ["king", "queen"] else 0.05

        flagged = scan_files(
            files=[self.test_file.name],
            exclude_terms=["nurse"],
            embedding=self.embedding,
            gender_direction=self.gender_direction,
            cutoff=0.1
        )

        self.assertTrue(any("king" in line or "queen" in line for line in flagged))
        self.assertFalse(any("nurse" in line for line in flagged))  # nurse is excluded

    def test_get_files_from_patterns_returns_files(self):
        pattern = os.path.dirname(self.test_file.name) + "/*.py"
        results = get_files_from_patterns([pattern])
        self.assertIn(self.test_file.name, results)


if __name__ == "__main__":
    unittest.main()
