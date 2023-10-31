# Kod testujący moduł.

import rect as r
from rect import point as p
import unittest

class TestRect(unittest.TestCase):
    def setUp(self):
        pass

    def test_str_rect(self):
        self.assertEqual(str(r.Rect(1, 2, 3, 4)), "[(1, 2), (3, 4)]")

    def test_repr_rect(self):
        self.assertEqual(repr(r.Rect(1, 2, 3, 4)), "Rect(1, 2, 3, 4)")

    def test_eq_rect(self):
        self.assertTrue(r.Rect(1, 2, 3, 4) == r.Rect(1, 2, 3, 4))

    def test_ne_rect(self):
        self.assertTrue(r.Rect(1, 2, 3, 4) != r.Rect(5, 6, 7, 8))

    def test_center_rect(self):
        self.assertEqual(r.Rect(1, 2, 3, 4).center(), p.Point(2, 3))

    def test_area_rect(self):
        self.assertEqual(r.Rect(1, 2, 3, 4).area(), 2 * 2)
        self.assertEqual(r.Rect(-2, -2, 2, 2).area(), 4 * 4)
        self.assertEqual(r.Rect(2, 2, -2, -2).area(), 4 * 4)
        self.assertEqual(r.Rect(-5, 5, -4, 4).area(), 1)
        self.assertEqual(r.Rect(5, -5, 4, -4).area(), 1)
        self.assertEqual(r.Rect(-5, 5, 4, -4).area(), 9 * 9)
        self.assertEqual(r.Rect(5, -5, -4, 4).area(), 9 * 9)

    def test_move_rect(self):
        self.assertEqual(r.Rect(0, 0, 1, 1).move(2, 4), r.Rect(2, 4, 3, 5))

    def tearDown(self): 
        pass

if __name__ == "__main__":
    print(r.Rect(1, 2, 3, 4))
    print([r.Rect(1, 2, 3, 4), r.Rect(5, 6, 7, 8)])
    unittest.main()  # wszystkie testy