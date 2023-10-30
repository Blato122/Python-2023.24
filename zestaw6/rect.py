from point import Point
from copy import deepcopy

class Rect:
    """Klasa reprezentująca prostokąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        """lewy dolny i prawy gorny wierzcholek"""
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    # "[(x1, y1), (x2, y2)]"
    def __str__(self):
        return "[{}, {}]".format(self.pt1, self.pt2)

    # "Rectangle(x1, y1, x2, y2)"
    def __repr__(self):
        return "{}({}, {}, {}, {})".format(self.__class__.__name__, self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y)

    # obsługa rect1 == rect2
    def __eq__(self, other):
        return ( (self.pt1 == other.pt1) and (self.pt2 == other.pt2) )

    # obsługa rect1 != rect2
    def __ne__(self, other):
        return not self == other

    # zwraca środek prostokąta
    def center(self):
        return Point((self.pt1.x + self.pt2.x) / 2, (self.pt1.y + self.pt2.y) / 2)

    # pole powierzchni
    def area(self):
        return abs(self.pt2.x - self.pt1.x) * abs(self.pt2.y - self.pt1.y)

    # przesunięcie o (x, y)
    def move(self, x, y):
        r = deepcopy(self)
        r.pt1.x += x
        r.pt2.x += x
        r.pt1.y += y
        r.pt2.y += y
        return r