# Kod testujący moduł.

from circle import Circle
import math
import unittest

class TestCircle(unittest.TestCase):
    def setUp(self):
        pass

    def test_radius_init_circle(self):
        self.assertRaises(ValueError, lambda: Circle(1, 1, -5))
        with self.assertRaises(ValueError) as ctx:
            Circle(2, 2, -8)

    def test_repr_circle(self):
        self.assertEqual(repr(Circle(1, 1, 5)), "Circle(1, 1, 5)")

    def test_eq_circle(self):
        self.assertTrue(Circle(1, 1, 5) == Circle(1, 1, 5))

    def test_ne_circle(self):
        self.assertTrue(Circle(1, 1, 5) != Circle(2, 2, 8))

    def test_area_circle(self):
        self.assertEqual(Circle(1, 1, 5).area(), 25 * math.pi)
        self.assertEqual(Circle(-1, 1, 0).area(), 0)
        self.assertEqual(Circle(1, -1, 0.5).area(), 0.25 * math.pi)

    def test_move_circle(self):
        self.assertEqual(Circle(1, 1, 5).move(2, 4), Circle(3, 5, 5))

    def test_cover_circle(self):
        result_r = (2.5 + math.sqrt(5)) / 2
        result = Circle(2, 1.5, result_r)
        self.assertEqual(Circle(1, 1, 1).cover(Circle(3, 2, 1.5)), result)

    def tearDown(self): 
        pass

if __name__ == "__main__":
    print(Circle(1, 1, 5))
    print([Circle(1, 1, 5), Circle(2, 2, 8)])
    unittest.main()  # wszystkie testy