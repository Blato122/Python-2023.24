import os
import sys
import math
import copy
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'zestaw6')) # :(
import point


class Circle:
    """Klasa reprezentująca okręgi na płaszczyźnie."""

    def __init__(self, x, y, r):
        if r < 0:
            raise ValueError("promień ujemny")
        self.pt = point.Point(x, y)
        self.r = r

    # "Circle(x, y, r)"
    def __repr__(self):
        return "{}({}, {}, {})".format(self.__class__.__name__, self.pt.x, self.pt.y, self.r)

    def __eq__(self, other):
        return self.pt == other.pt and self.r == other.r

    def __ne__(self, other):
        return not self == other

    # pole powierzchni
    def area(self):
        return math.pi * self.r * self.r     

    # przesuniecie o (x, y)
    def move(self, x, y):
        c = copy.deepcopy(self)
        c.pt.x += x
        c.pt.y += y
        return c

    # najmniejszy okrąg pokrywający oba
    def cover(self, other):
        x = (self.pt.x + other.pt.x) / 2
        y = (self.pt.y + other.pt.y) / 2
        center_dist = math.sqrt((self.pt.x - other.pt.x)**2 + (self.pt.y - other.pt.y)**2)
        r = (self.r + other.r + center_dist) / 2
        return Circle(x, y, r)