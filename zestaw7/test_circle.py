# Kod testujący moduł.

import circle as c
from circle import point as p
import math
import unittest

class TestCircle(unittest.TestCase):
    def setUp(self):
        pass

    def test_radius_init_circle(self):
        self.assertRaises(ValueError, lambda: c.Circle(1, 1, -5))
        with self.assertRaises(ValueError) as ctx:
            c.Circle(2, 2, -8)

    def test_repr_circle(self):
        self.assertEqual(repr(c.Circle(1, 1, 5)), "Circle(1, 1, 5)")

    def test_eq_circle(self):
        self.assertTrue(c.Circle(1, 1, 5) == c.Circle(1, 1, 5))

    def test_ne_circle(self):
        self.assertTrue(c.Circle(1, 1, 5) != c.Circle(2, 2, 8))

    def test_area_circle(self):
        self.assertEqual(c.Circle(1, 1, 5).area(), 25 * math.pi)
        self.assertEqual(c.Circle(-1, 1, 0).area(), 0)
        self.assertEqual(c.Circle(1, -1, 0.5).area(), 0.25 * math.pi)

    def test_move_circle(self):
        self.assertEqual(c.Circle(1, 1, 5).move(2, 4), c.Circle(3, 5, 5))

    def test_cover_circle(self):
        result_r = (2.5 + math.sqrt(5)) / 2
        result = c.Circle(2, 1.5, result_r)
        self.assertEqual(c.Circle(1, 1, 1).cover(c.Circle(3, 2, 1.5)), result)

    def tearDown(self): 
        pass

if __name__ == "__main__":
    print(c.Circle(1, 1, 5))
    print([c.Circle(1, 1, 5), c.Circle(2, 2, 8)])
    unittest.main()  # wszystkie testy