import unittest
from bias_detector.scoring import cosine

class TestScoring(unittest.TestCase):
    def test_cosine(self):
        u_vector = [1, 0]
        v_vector = [0, 1]
        result = cosine(u_vector, v_vector)
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()