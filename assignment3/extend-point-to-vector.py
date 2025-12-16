import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        return False

    def __str__(self):
        return "Point(" + str(self.x) + ", " + str(self.y) + ")"

    def distance_to(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return math.sqrt(dx * dx + dy * dy)


class Vector(Point):
    def __str__(self):
        return "Vector(" + str(self.x) + ", " + str(self.y) + ")"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)


p1 = Point(3, 4)
p2 = Point(6, 8)

print(p1)
print(p1 == p2)
print(p1.distance_to(p2))

v1 = Vector(2, 5)
v2 = Vector(3, 4)

v3 = v1 + v2
print(v3)
