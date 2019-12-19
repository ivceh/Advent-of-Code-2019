import sys
import os
sys.path.append(os.getcwd() + "/..")
from Geometry import *
from collections import deque
import heapq

# reading input
with open("input.txt", "r") as file:
    A = [list(line) for line in file.read().splitlines()]

# counting keys and finding the entrance
keys_num = 0
for i, line in enumerate(A):
    for j, pos in enumerate(line):
        if "a" <= pos <= "z":
            keys_num += 1
        elif pos == "@":
            entrances1 = [Point2D(j, i)]

def value(p):
    return A[p.y][p.x]

def set_value(p, c):
    A[p.y][p.x] = c

# breadth-first search to find distances to all keys accessible from arbitrary point
def small_bfs(point, collected):
    Q = deque([(0, point)])
    visited_small = {point}
    while Q:
        for d in Direction:
            next_point = move_point(Q[0][1], d)
            if next_point in visited_small or value(next_point) == "#":
                continue
            elif "a" <= value(next_point) <= "z" and value(next_point) not in collected:
                yield Q[0][0] + 1, next_point
            elif "A" <= value(next_point) <= "Z" and value(next_point).lower() not in collected:
                continue
            else:
                Q.append((Q[0][0] + 1, next_point))
                visited_small.add(next_point)
        Q.popleft()

# Dijkstra's algorithm to solve the problem
def Dijkstra(entrances):
    H = [(0, entrances, set())]
    visited = {(tuple(entrances), frozenset()): 0}
    while H:
        dist, points, keys = heapq.heappop(H)
        if len(keys) == keys_num:
            return dist
        elif visited[(tuple(points), frozenset(keys))] == dist:
            for i, point in enumerate(points):
                for dist2, next_point in small_bfs(point, keys):
                    keys2 = keys.copy()
                    keys2.add(value(next_point))
                    points2 = points.copy()
                    points2[i] = next_point
                    visited_tuple = (tuple(points2), frozenset(keys2))
                    if visited_tuple not in visited or dist + dist2 < visited[visited_tuple]:
                        heapq.heappush(H, (dist + dist2, points2, keys2))
                        visited[visited_tuple] = dist + dist2

# solving Part 1
print("Part 1:", Dijkstra(entrances1))

entrances2 = []
for i in (-1, 0, 1):
    for j in (-1, 0, 1):
        set_value(entrances1[0] + Point2D(i, j), "#")
for i in (-1, 1):
    for j in (-1, 1):
        set_value(entrances1[0] + Point2D(i, j), "@")
        entrances2.append(entrances1[0] + Point2D(i, j))

# solving Part 2
print("Part 2:", Dijkstra(entrances2))
