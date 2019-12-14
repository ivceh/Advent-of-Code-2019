import sys
import os
sys.path.append(os.getcwd() + "/..")
from Intcode_computer import *
from Geometry import *

class Tile(IntEnum):
    empty = 0
    wall = 1
    block = 2
    paddle = 3
    ball = 4

class State(IntEnum):
    read_x = 0
    read_y = 1
    read_tile_id = 2

def next_state(s):
    return State((s + 1) % 3)

grid = {}
s = State.read_x

def out_func(out):
    global grid, x, y, s
    if s == State.read_x:
        x = out
    elif s == State.read_y:
        y = out
    elif s == State.read_tile_id:
        grid[Point2D(x, y)] = Tile(out)
    else:
        raise ValueError("Unknown state!")
    s = next_state(s)

# reading input
with open("input.txt", "r") as file:
    A = [int(a) for a in file.read().split(',')]

# solving Part 1
p = program(A, None, out_func)
p.exec()
print("Part 1:", sum(1 for val in grid.values() if val == Tile.block))

# solving Part 2
paddlex = next(key for key, val in grid.items() if val == Tile.paddle).x
def sgn(x):
    if x > 0:
        return 1
    elif x == 0:
        return 0
    else:
        return -1

# moving paddle towards the ball
def in_func2():
    global ball, paddlex
    direction = sgn(x - paddlex)
    paddlex += direction
    return direction

def out_func2(out):
    global s, x, y, score
    if s == State.read_x:
        x = out
    elif s == State.read_y:
        y = out
    elif s == State.read_tile_id:
        score = out
    else:
        raise ValueError("Unknown state!")
    s = next_state(s)
    
s = State.read_x
A[0] = 2
p = program(A, in_func2, out_func2)
p.exec()
print("Part 2:", score)
