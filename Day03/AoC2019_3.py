import sys
import os
sys.path.append(os.getcwd() + "/..")
from Geometry import *

# read input
with open("input.txt", "r") as file:
    A = [(Direction(s[0]), int(s[1:])) for s in file.readline().split(',')]
    B = [(Direction(s[0]), int(s[1:])) for s in file.readline().split(',')]

# goes through coordinates of the wire
def go(wire):
    pos = Point2D(0, 0)
    steps = 0
    for direction, length in wire:
        for i in range(length):
            pos = move_point(pos, direction)
            steps += 1
            yield (pos, steps)

# key: coordinates of the first wire
# value: number of steps
wireA = dict()

# fill wireA dictionary
for pos, steps in go(A):
    if not pos in wireA:
        wireA[pos] = steps

# check for intersection between wires
inter_dists = []
inter_steps = []
for pos, steps in go(B):
    if pos in wireA:
        inter_dists.append(norm1(pos))
        inter_steps.append(wireA[pos] + steps)

# output
print("Part One:", min(inter_dists))
print("Part Two:", min(inter_steps))
