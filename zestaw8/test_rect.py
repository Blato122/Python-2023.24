from rect import Rect
from rect import point
from point import Point
import pytest

def test_properties_rect():
    rect = Rect(1, 2, 4, 5)

    assert rect.top == 5
    assert rect.left == 1
    assert rect.bottom == 2
    assert rect.right == 4
    assert rect.width == 4 - 1
    assert rect.height == 5 - 2
    assert rect.topleft == Point(1, 5)
    assert rect.bottomleft == Point(1, 2)
    assert rect.topright == Point(4, 5)
    assert rect.bottomright == Point(4, 2)

def test_from_points_rect():
    pt1 = Point(1, 2)
    pt2 = Point(4, 5)
    rect = Rect.from_points((pt1, pt2))

    assert rect.top == 5
    assert rect.left == 1
    assert rect.bottom == 2
    assert rect.right == 4
    assert rect.width == 4 - 1
    assert rect.height == 5 - 2
    assert rect.topleft == Point(1, 5)
    assert rect.bottomleft == pt1
    assert rect.topright == pt2
    assert rect.bottomright == Point(4, 2)

def test_str_rect():
    assert str(Rect(1, 2, 3, 4)) == "[(1, 2), (3, 4)]"

def test_repr_rect():
    assert repr(Rect(1, 2, 3, 4)) == "Rect(1, 2, 3, 4)"

def test_eq_rect():
    assert Rect(1, 2, 3, 4) == Rect(1, 2, 3, 4)

def test_ne_rect():
    assert Rect(1, 2, 3, 4) != Rect(5, 6, 7, 8)

def test_center_rect():
    assert Rect(1, 2, 3, 4).center() == Point(2, 3)

def test_area_rect():
    assert Rect(1, 2, 3, 4).area() == 2 * 2
    assert Rect(-2, -2, 2, 2).area() == 4 * 4
    assert Rect(2, 2, -2, -2).area() == 4 * 4
    assert Rect(-5, 5, -4, 4).area() == 1
    assert Rect(5, -5, 4, -4).area() == 1
    assert Rect(-5, 5, 4, -4).area() == 9 * 9
    assert Rect(5, -5, -4, 4).area() == 9 * 9

def test_move_rect():
    assert Rect(0, 0, 1, 1).move(2, 4) == Rect(2, 4, 3, 5)

if __name__ == "__main__":
    pytest.main()