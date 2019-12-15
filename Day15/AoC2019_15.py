import sys
import os
sys.path.append(os.getcwd() + "/..")
from Intcode_computer import *
from Geometry import *
from copy import deepcopy
from collections import deque

# reading input
with open("input.txt", "r") as file:
    A = [int(a) for a in file.read().split(',')]

direction = [None,
             Direction.up,
             Direction.down,
             Direction.right,
             Direction.left]

def in_func():
    return in_value

out_values = ["#", ".", "O"]
def out_func(x):
    global oxygen_pos
    visited[Q[-1][0]] = out_values[x]
    if x == 0:     # wall
        Q.pop()
    elif x == 1:   # successful move
        pass
    elif x == 2:   # oxygen
        print("Part 1:", Q[-1][2])
        oxygen_pos = Q[-1][0]
    else:
        raise ValueError("Unknown output value")

# solving Part 1 using breadth first search
p = program(A, in_func, out_func)
Q = deque([(Point2D(0, 0), p, 0)])
p.exec_until_input()
visited = {Point2D(0, 0): "D"}
while Q:
    if Q[0][1].opcode != 99:
        for d in range(1, 5):
            next_point = move_point(Q[0][0], direction[d])
            if next_point not in visited:
                p = deepcopy(Q[0][1])
                in_value = d
                p.step()
                Q.append((next_point, p, Q[0][2] + 1))
                p.exec_until_input()
    Q.popleft()

# solving Part 2 using another breadth first search starting from oxygen_pos
Q2 = deque([(oxygen_pos, 0)])
visited2 = set([oxygen_pos])
while Q2:
    for d in range(4):
        next_point = move_point(Q2[0][0], d)
        if next_point not in visited2 and visited[next_point] != "#":
            visited2.add(next_point)
            Q2.append((next_point, Q2[0][1] + 1))
    if len(Q2) == 1:
        print("Part 2:", Q2[0][1])
    Q2.popleft()

# drawing map
print("Bonus, map:")
minx = min(pos.x for pos in visited.keys())
maxx = max(pos.x for pos in visited.keys())
miny = min(pos.y for pos in visited.keys())
maxy = max(pos.y for pos in visited.keys())
for i in range(miny, maxy + 1):
    for j in range(minx, maxx + 1):
        if (j, i) in visited:
            print(visited[(j, i)], end="")
        else:
            print(" ", end="")
    print()
            
