import unittest
from equation import solv
import math


class TestSolv(unittest.TestCase):

    def test_normal_case(self):
        res = solv(9, 5, 7, 3)
        self.assertAlmostEqual(res, 0.5)

    def test_zero_under_root_boundary(self):
        res = solv(5, 5, 10, 8)
        self.assertAlmostEqual(res, 0.0)

    def test_negative_under_root_raises(self):
        with self.assertRaises(ValueError):
            solv(3, 5, 10, 8)

    def test_division_by_zero_raises(self):
        with self.assertRaises(ValueError):
            solv(9, 4, 7, 7)

    def test_float_values(self):
        res = solv(5.5, 1.5, 4.0, 1.0)
        expe = math.sqrt(5.5 - 1.5) / (4.0 - 1.0)
        self.assertAlmostEqual(res, expe)


if __name__ == "__main__":
    unittest.main()
