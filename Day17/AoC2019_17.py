import sys
import os
sys.path.append(os.getcwd() + "/..")
from Intcode_computer import *
from Geometry import *
from collections import deque
from copy import deepcopy

# reading input
with open("input.txt", "r") as file:
    A = [int(a) for a in file.read().split(",")]

# solving Part 1
def value(pos):
    if pos.y < 0 or pos.y >= len(grid) or pos.x < 0 or pos.x >= len(grid[pos.y]):
        return "."
    return grid[pos.y][pos.x]

grid = []
line = ""
def out_func(x):
    global grid, line
    c = str(chr(x))
    if c == "\n":
        if line != "":
            grid.append(line)
        line = ""
    else:
        line += chr(x)

p = program(A, None, out_func)
p.exec()

s = 0
for i in range(1, len(grid) - 1):
    for j in range(1, len(grid[i]) - 1):
        if grid[i][j] != "." and not any(value(move_point(Point2D(j, i), d)) == "." for d in list(Direction)):
            s += i * j

print("Part 1:", s)

# solving Part 2
# splitting into smaller parts done manually
arrow_dir = {
    "<": Direction.left,
    ">": Direction.right,
    "^": Direction.up,
    "v": Direction.down
}

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] in arrow_dir:
            robot = Point2D(j,i)
            direction = arrow_dir[grid[i][j]]

cnt = 0
first = True
while True:
    next_point = move_point(robot, direction)
    if value(next_point) == "#":
        cnt += 1
    else:
        if first:
            first = False
        else:
            print(",", end = "")
        print(cnt, end = "")
        cnt = 1
        next_point = move_point(robot, turn_left(direction))
        if value(next_point) == "#":
            direction = turn_left(direction)
            print(",L", end = "")
        else:
            next_point = move_point(robot, turn_right(direction))
            if value(next_point) == "#":
                direction = turn_right(direction)
                print(",R", end = "")
            else:
                break
    robot = next_point

# Splitting done manually using previous output
s = ("A,C,A,C,B,B,C,A,C,B\n"
"L,4,R,8,L,6,L,10\n"
"L,4,L,4,L,10\n"
"L,6,R,8,R,10,L,6,L,6\n"
"y\n")

spos = 0
def in_func2():
    global spos, s
    spos += 1
    return ord(s[spos - 1])

def out_func2(x):
    global sol
    sol = x

A[0] = 2
p2 = program(A, in_func2, out_func2)
p2.exec()
print("\nPart 2:", sol)
