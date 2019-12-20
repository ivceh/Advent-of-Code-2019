import sys
import os
sys.path.append(os.getcwd() + "/..")
from Intcode_computer import *
from Geometry import *
from itertools import count

# reading input
with open("input.txt", "r") as file:
    A = [int(a) for a in file.read().split(",")]

def out_func(x):
    global s
    s = bool(x)

grid = {}
def value(point):
    #if point.x % 10 == point.y % 10 == 0:
    #    print(point)
    if point in grid:
        return grid[point]
    else:
        inputQ.append(point.x)
        inputQ.append(point.y)
        p = program(A, input_from_queue(), out_func)
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
