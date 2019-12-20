import sys
import os
sys.path.append(os.getcwd() + "/..")
from Geometry import *
from collections import deque

# reading input
with open("input.txt", "r") as file:
    A = file.read().splitlines()

def value(p):
    if p.y < 0 or p.y >= len(A) or p.x < 0 or p.x >= len(A[p.y]):
        return "#"
    return A[p.y][p.x]

portals = {}

for i, line in enumerate(A):
    for j, pos in enumerate(line):
        if "A" <= pos <= "Z":
            if "A" <= value(Point2D(j, i + 1)) <= "Z":
                portal = frozenset({pos, value(Point2D(j, i + 1))})
                if value(Point2D(j, i - 1)) == ".":
                    entrance = Point2D(j, i - 1)
                else:
                    entrance = Point2D(j, i + 2)
                if portal in portals:
                    portals[portal].append(entrance)
                else:
                    portals[portal] = [entrance]
            elif "A" <= value(Point2D(j + 1, i)) <= "Z":
                portal = frozenset({pos, value(Point2D(j + 1, i))})
                if value(Point2D(j - 1, i)) == ".":
                    entrance = Point2D(j - 1, i)
                else:
                    entrance = Point2D(j + 2, i)
                if portal in portals:
                    portals[portal].append(entrance)
                else:
                    portals[portal] = [entrance]

# breadth first search
# input: function for neighbours of arbitrary point, start, end
# output: minimal number of steps from start to end
def bfs(neighbours, start, end):
    Q = deque([(start, 0)])
    visited = {start}
    while Q:
        p, dist = Q.popleft()
        for p2 in neighbours(p):
            if p2 not in visited:
                if p2 == end:
                    return dist + 1
                Q.append((p2, dist + 1))
                visited.add(p2)

# solving Part 1
def neighbours1(p):
    for d in Direction:
        p2 = move_point(p, d)
        if value(p2) == "#":
            continue
        elif "A" <= value(p2) <= "Z":
            portal = frozenset({value(p2), value(move_point(p2, d))})
            if portal != frozenset({"A"}):
                if portals[portal][0] == p:
                    yield portals[portal][1]
                else:
                    yield portals[portal][0]
        else:
            yield  p2

print("Part 1:", bfs(neighbours1,
                     portals[frozenset({"A"})][0],
                     portals[frozenset({"Z"})][0]))

# solving Part 2
def outer(p):
    return p.y < 5 or p.y >= len(A) - 5 or p.x < 5 or p.x >= len(A[p.y]) - 5

def neighbours2(p):
    point, level = p
    for d in Direction:
        point2 = move_point(point, d)
        if value(point2) == "#":
            continue
        elif "A" <= value(point2) <= "Z":
            portal = frozenset({value(point2), value(move_point(point2, d))})
            if portal not in (frozenset({"A"}), frozenset({"Z"})):
                if outer(point2):
                    level2 = level - 1
                else:
                    level2 = level + 1
                if level2 >= 0:
                    if portals[portal][0] == point:
                        yield portals[portal][1], level2
                    else:
                        yield portals[portal][0], level2
        else:
            yield point2, level

print("Part 2:", bfs(neighbours2,
                     (portals[frozenset({"A"})][0], 0),
                     (portals[frozenset({"Z"})][0], 0)))
