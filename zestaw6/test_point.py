# Kod testujący moduł.

import point as p
import unittest

class TestPoint(unittest.TestCase):
    def setUp(self):
        pass

    def test_str_point(self):
        self.assertEqual(str(p.Point(1, 2)), "(1, 2)")

    def test_repr_point(self):
        self.assertEqual(repr(p.Point(1, 2)), "Point(1, 2)")

    def test_eq_point(self):
        self.assertTrue(p.Point(1, 2) == p.Point(1, 2))

    def test_ne_point(self):
        self.assertTrue(p.Point(1, 2) != p.Point(3, 4))

    def test_add_point(self):
        self.assertEqual(p.Point(1, 2) + p.Point(3, 4), p.Point(4, 6))

    def test_neg_point(self):
        self.assertEqual(-p.Point(1, 2), p.Point(-1, -2))

    def test_sub_point(self):
        self.assertEqual(p.Point(1, 2) - p.Point(3, 4), p.Point(-2, -2))

    def test_mul_point(self):
        self.assertEqual(p.Point(1, 2) * p.Point(3, 4), 3 + 8)

    def test_cross_point(self):
        self.assertEqual(p.Point(1, 2).cross(p.Point(3, 4)), 4 - 6)

    def test_length_point(self):
        self.assertEqual(p.Point(3, 4).length(), 5)

    def test_hash_point(self):
        pass

    def tearDown(self): 
        pass

if __name__ == "__main__":
    unittest.main()  # wszystkie testy