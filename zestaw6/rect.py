from point import Point

class Rectangle:
    """Klasa reprezentująca prostokąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        """lewy dolny i prawy gorny wierzcholek"""
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    # "[(x1, y1), (x2, y2)]"
    def __str__(self):
        return "({}, {})".format(self.pt1, self.pt2) # ?

    def __repr__(self):         # "Rectangle(x1, y1, x2, y2)"
        return "Rectangle({}, {})".format(repr(self.pt1), repr(self.pt2))

    # obsługa rect1 == rect2
    def __eq__(self, other):
        return ( (self.pt1 == other.pt1) and (self.pt2 == other.pt2) )

    # obsługa rect1 != rect2
    def __ne__(self, other):
        return not self == other

    def center(self): pass          # zwraca środek prostokąta

    def area(self): pass            # pole powierzchni

    def move(self, x, y): pass      # przesunięcie o (x, y)