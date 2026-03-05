import unittest
from comparator import compare

class ComparatorTest(unittest.TestCase):
    def test_a_gt_b(self):
        self.assertEqual(1, compare(7, 3))

    def test_a_lt_b(self):
        self.assertEqual(-1, compare(3, 7))

    def test_a_eq_b(self):
        self.assertEqual(0, compare(7, 7))

if __name__ == "__main__":
    unittest.main()
