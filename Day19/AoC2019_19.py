import sys
import os
sys.path.append(os.getcwd() + "/..")
from Intcode_computer import *
from Geometry import *
from itertools import count

# reading input
with open("input.txt", "r") as file:
    A = [int(a) for a in file.read().split(",")]

class State(IntEnum):
    X = 0
    Y = 1

def other_state(s):
    return State(1 - s)

state = State.X
x = 0
y = 0
def in_func():
    global state, x, y, s
    if state == State.X:
        retval = x
    else:
        retval = y
    state = other_state(state)
    return retval

def out_func(x):
    global s
    s = bool(x)

grid = {}
def value(point):
    if point in grid:
        return grid[point]
    else:
        global x, y
        x = point.x
        y = point.y
        p = program(A, in_func, out_func)
        p.exec()
        grid[point] = s
        return s

# solving Part 1
print("Part 1:", sum(sum(value(Point2D(i, j))
                         for i in range(50))
                     for j in range(50)))

# solving Part 2
def nonnegative_points():
    for i in count():
        for j in range(i + 1):
            yield Point2D(j, i - j)
            
def square100_100(point):
    return all(all(value(point + Point2D(i, j))
                   for j in range(100))
               for i in range(100))

for point in nonnegative_points():
    if square100_100(point):
        print("Part 2:", 10000 * point.x + point.y)
        break
