import os
import sys
import copy
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "zestaw6")) # :(
import point

class Rect:
    """Klasa reprezentująca prostokąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        """lewy dolny i prawy gorny wierzcholek"""
        self.__pt1 = point.Point(x1, y1)
        self.__pt2 = point.Point(x2, y2)

        self.__bottom = y1
        self.__top = y2
        self.__left = x1
        self.__right = x2
        self.__width = abs(x2 - x1)
        self.__height = abs(y2 - y1)

        self.__topleft = point.Point(x1, y2)
        self.__bottomleft = self.__pt1
        self.__topright = self.__pt2
        self.__bottomright = point.Point(x2, y1)

    @property
    def bottom(self):   # getting an attribute value
        return self.__bottom
        
    @property
    def top(self):   # getting an attribute value
        return self.__top

    @property
    def left(self):   # getting an attribute value
        return self.__left

    @property
    def right(self):   # getting an attribute value
        return self.__right

    @property
    def width(self):   # getting an attribute value
        return self.__width

    @property
    def topleft(self):   # getting an attribute value
        return self.__topleft

    @property
    def height(self):   # getting an attribute value
        return self.__height

    @property
    def bottomleft(self):   # getting an attribute value
        return self.__bottomleft

    @property
    def topright(self):   # getting an attribute value
        return self.__topright

    @property
    def bottomright(self):   # getting an attribute value
        return self.__bottomright

    @classmethod
    def from_points(cls, pts):
        left = min(p.x for p in pts)
        right = max(p.x for p in pts)
        bottom = min(p.y for p in pts)
        top = max(p.y for p in pts)
        return cls(left, bottom, right, top)

    # "[(x1, y1), (x2, y2)]"
    def __str__(self):
        return "[{}, {}]".format(self.__pt1, self.__pt2)

    # "Rectangle(x1, y1, x2, y2)"
    def __repr__(self):
        return "{}({}, {}, {}, {})".format(self.__class__.__name__, self.__pt1.x, self.__pt1.y, self.__pt2.x, self.__pt2.y)

    # obsługa rect1 == rect2
    def __eq__(self, other):
        return ( (self.__pt1 == other.__pt1) and (self.__pt2 == other.__pt2) )

    # obsługa rect1 != rect2
    def __ne__(self, other):
        return not self == other

    # zwraca środek prostokąta
    def center(self):
        return point.Point((self.__pt1.x + self.__pt2.x) / 2, (self.__pt1.y + self.__pt2.y) / 2)

    # pole powierzchni
    def area(self):
        return abs(self.__pt2.x - self.__pt1.x) * abs(self.__pt2.y - self.__pt1.y)

    # przesunięcie o (x, y)
    def move(self, x, y):
        r = copy.deepcopy(self)
        r.__pt1.x += x
        r.__pt2.x += x
        r.__pt1.y += y
        r.__pt2.y += y
        return r