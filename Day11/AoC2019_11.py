import sys
import os
sys.path.append(os.getcwd() + "/..")
from Intcode_computer import *
from Geometry import *

# reading input
with open("input.txt", "r") as file:
    A = [int(a) for a in file.read().split(',')]

class State(IntEnum):
    paint = 0
    turn = 1

def other_state(s):
    return State(1 - s)

class Color(IntEnum):
    black = 0
    white = 1

def turn(left0right1):
    global direction
    if left0right1 == 0:
        direction = turn_left(direction)
    elif left0right1 == 1:
        direction = turn_right(direction)
    else:
        raise ValueError("Unknown direction!")

def paint(color):
    grid[pos] = color

def in_func():
    if pos in grid:
        return grid[pos]
    else:
        return Color.black

def out_func(x):
    global pos, state
    if state == State.paint:
        paint(x)
    elif state == State.turn:
        turn(x)
        pos = move_point(pos, direction)
    else:
        raise ValueError("Unknown state!")
    state = other_state(state)

def exec(g):
    global grid, pos, state, direction
    grid = g
    pos = Point2D(0, 0)
    state = State.paint
    direction = Direction.up
    p = program(A, in_func, out_func)
    p.exec()

exec({})
print("Part 1:", len(grid))

exec({Point2D(0, 0): Color.white})
minx = min(pos.x for pos, color in grid.items() if color == Color.white)
maxx = max(pos.x for pos, color in grid.items() if color == Color.white)
miny = min(pos.y for pos, color in grid.items() if color == Color.white)
maxy = max(pos.y for pos, color in grid.items() if color == Color.white)
print("Part 2:")
for i in range(miny, maxy + 1):
    for j in range(minx, maxx + 1):
        if (j,i) in grid and grid[(j,i)] == Color.white:
            print("#", end="")
        else:
            print(" ", end="")
    print()
