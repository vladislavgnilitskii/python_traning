from math import sqrt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, p2):
        dx = p2.x - self.x
        dy = p2.y - self.y
        return sqrt(dx * dx + dy * dy)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


a = Point(0,0)
b = Point(3, 4)
print(a.distance(b))
print(a == b)
print(a == Point(0, 0))

