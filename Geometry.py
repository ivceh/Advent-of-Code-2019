from collections import namedtuple
from enum import IntEnum

class Point2D(namedtuple("Point", ("x", "y"))):
    def __add__(self, other):
        return Point2D(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return Point2D(self.x - other.x, self.y - other.y)

class Point3D(namedtuple("Point", ("x", "y", "z"))):
    def __add__(self, other):
        return Point3D(self.x + other.x, self.y + other.y, self.z + other.z)
    def __sub__(self, other):
        return Point3D(self.x - other.x, self.y - other.y, self.z - other.z)

def dist_sqr(p, p2 = None):
    if p2 is None:
        return sum(d ** 2 for d in p)
    else:
        return dist_sqr(p2 - p)

def norm1(p, p2 = None):
    if p2 is None:
        return sum(abs(d) for d in p)
    else:
        return norm1(p2 - p)

class Direction(IntEnum):
    up = 0
    right = 1
    down = 2
    left = 3

    @classmethod
    def _missing_(self, s):
        if isinstance(s, str):
            s = s.lower()
            if s == "u" or s == "up":
                return Direction.up
            elif s == "r" or s == "right":
                return Direction.right
            elif s == "d" or s == "down":
                return Direction.down
            elif s == "l" or s == "left":
                return Direction.left
            else:
                return ValueError("Unknown direction name")
        else:
            return super()._missing_(s)

def turn_left(d):
    return Direction((d + 3) % 4)

def turn_right(d):
    return Direction((d + 1) % 4)

def move_point(p, d):
    if d == Direction.up:
        return Point2D(p.x, p.y - 1)
    elif d == Direction.right:
        return Point2D(p.x + 1, p.y)
    elif d == Direction.down:
        return Point2D(p.x, p.y + 1)
    elif d == Direction.left:
        return Point2D(p.x - 1, p.y)
    else:
        raise ValueError("Unknown direction!")
