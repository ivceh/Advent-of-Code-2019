import sys
import os
sys.path.append(os.getcwd() + "/..")
from Geometry import *
import re
import math

# reading input
A = []
with open('input.txt') as file:
    for line in file.read().splitlines():
        matchObj = re.match(r'<x=(-?\d+), y=(-?\d+), z=(-?\d+)>', line)
        A.append(Point3D(*(int(matchObj.group(i)) for i in range(1, 4))))

V = [Point3D(0, 0, 0) for _ in A]
A0 = A.copy()
V0 = V.copy()

def sgn(x):
    if x > 0:
        return 1
    elif x == 0:
        return 0
    else:
        return -1

def step(A, V):
    for i, ai in enumerate(A):
        for aj in A:
            V[i] += Point3D(*(sgn(ajd - aid) for aid, ajd in zip(ai, aj)))
    for i, vi in enumerate(V):
        A[i] += vi

# solving Part 1
for _ in range(1000):
    step(A, V)
print("Part 1:", sum(norm1(ai) * norm1(vi) for ai, vi in zip(A, V)))

# solving Part 2
# There are 3 independent parts of the simulation for 3 axes.
# We will find the period for each of them.
# Least common multiple of those 3 periods will be the total period.

def lcm(a, b, c = None):
    if c is None:
        return a * (b // math.gcd(a, b))
    else:
        return lcm(lcm(a, b), c)

A = A0.copy()
V = V0.copy()
coordinate_periods = [None] * 3
steps = 0
while any(period is None for period in coordinate_periods):
    step(A, V)
    steps += 1
    for coord in range(3):
        if coordinate_periods[coord] is None:
            if all(a[coord] == a0[coord] for a, a0 in zip(A, A0)) and \
              all(v[coord] == v0[coord] for v, v0 in zip(V, V0)):
                coordinate_periods[coord] = steps
print("Part 2:", lcm(*(coordinate_periods)))
