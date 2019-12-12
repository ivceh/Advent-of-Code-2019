import sys
import os
sys.path.append(os.getcwd() + "/..")
from Intcode_computer import *

# reading input
with open("input.txt", "r") as file:
    A = [int(a) for a in file.read().split(',')]

print("Part 1:", end = " ")
p = program(A, lambda: 1, lambda x: print(x))
p.exec()

print("Part 2:", end = " ")
p = program(A, lambda: 2, lambda x: print(x))
p.exec()

