import os
import sys
import math
import copy
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "zestaw6")) # :(
import point
from operator import add

# __file__ attribute is used to get the name of the file being executed. 
# Then os.path.dirname() is used to get the path of the parent directory. 
# We then use os.path.join to move up one directly (i.e., ..) and 
# into the 'zestaw6' sibling directory. Finally, we append this path to sys.path.

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

    def __round__(self):
        return Circle(round(self.pt.x, ndigits=9), 
                      round(self.pt.y, ndigits=9), 
                      round(self.r, ndigits=9))

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

        center_dist = math.sqrt((self.pt.x - other.pt.x)**2 + (self.pt.y - other.pt.y)**2)

        # pierwszy okrag zawiera sie w drugim okregu -> zwroc wiekszy okrag (drugi)
        if (self.r + center_dist <= other.r):
            x, y, r = other.pt.x, other.pt.y, other.r
        # drugi okrag zawiera sie w pierwszym okregu -> zwroc wiekszy okrag (pierwszy)
        elif (other.r + center_dist <= self.r):
            x, y, r = self.pt.x, self.pt.y, self.r
        # brak zawierania okregow
        elif (self.r + center_dist > other.r):
            r = (self.r + other.r + center_dist) / 2
            # nowy srodek musi lezec na odcinku laczacym srodki dwoch okregow
            theta = 1/2 + (other.r - self.r) / (2 * center_dist)
            x = (1-theta)*self.pt.x + theta*other.pt.x
            y = (1-theta)*self.pt.y + theta*other.pt.y
        else:
            r = (self.r + other.r + center_dist) / 2
            # nowy srodek musi lezec na odcinku laczacym srodki dwoch okregow
            theta = 1/2 + (self.r - other.r) / (2 * center_dist)
            x = (1-theta)*other.pt.x + theta*self.pt.x
            y = (1-theta)*other.pt.y + theta*self.pt.y

        return Circle(x, y, r)