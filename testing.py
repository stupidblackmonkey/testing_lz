import unittest
from equation import solv
import math


class TestSolv(unittest.TestCase):

    def test_normal_case(self):
        result = solv(9, 5, 7, 3)
        self.assertAlmostEqual(result, 0.5)

    def test_zero_under_root_boundary(self):
        result = solv(5, 5, 10, 8)
        self.assertAlmostEqual(result, 0.0)

    def test_negative_under_root_raises(self):
        with self.assertRaises(ValueError):
            solv(3, 5, 10, 8)

    def test_division_by_zero_raises(self):
        with self.assertRaises(ValueError):
            solv(9, 4, 7, 7)

    def test_float_values(self):
        result = solv(5.5, 1.5, 4.0, 1.0)
        expected = math.sqrt(5.5 - 1.5) / (4.0 - 1.0)
        self.assertAlmostEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
