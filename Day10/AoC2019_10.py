import sys
import os
sys.path.append(os.getcwd() + "/..")
from Geometry import *

def same_direction(d1, d2):
    return d1.x * d2.y == d1.y * d2.x and (d1.x * d2.x > 0 or
                                           d1.y * d2.y > 0)

# reading input
with open("input.txt", "r") as file:
    A = file.read().splitlines()

# solving Part 1
max_visible = 0
for i, row in enumerate(A):
    for j, point in enumerate(row):
        if point == "#":
            # list of directions of asteroids visible from (j, i)
            directions = []
            for k, row2 in enumerate(A):
                for l, point2 in enumerate(row2):
                    if point2 == "#" and (k != i or l != j):
                        d = Point2D(l - j, k - i)
                        same_direction_found = any(same_direction(d, d2)
                                                   for d2 in directions)
                        if not same_direction_found:
                            directions.append(d)
            if len(directions) > max_visible:
                max_visible = len(directions)
                max_directions = directions
                max_point = Point2D(j, i)
print("Part 1:", max_visible)

# solving Part 2

# input: direction vector
# output: (quadrant, value to sort directions in the same quadrant)
def sort_key(d):
    if d.x >= 0 and d.y < 0:
        return (1, d.x / d.y)
    elif d.x > 0 and d.y >= 0:
        return (2, d.y / d.x)
    elif d.x <= 0 and d.y > 0:
        return (3, d.x / d.y)
    elif d.x < 0 and d.y <= 0:
        return (4, d.y / d.x)
    else:
        raise ValueError("Direction vector " + str(d))

# finding 200th direction
l = list(max_directions)
l.sort(key = sort_key)
dir200 = l[199]

# finding the closest point in that direction
min_dist_sqr = dist_sqr((len(A), len(A[0])))
for i, row in enumerate(A):
    for j, point in enumerate(row):
        if point == "#":
            d = Point2D(j, i) - max_point
            if same_direction(d, dir200):
                if dist_sqr(d) < min_dist_sqr:
                    min_dist_sqr = dist_sqr(d)
                    point2 = Point2D(j, i)

print("Part 2:", point2.x * 100 + point2.y)

