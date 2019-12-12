import sys
import os
sys.path.append(os.getcwd() + "/..")
from Intcode_computer import *

# reading input
with open("input.txt", "r") as file:
    A = [int(a) for a in file.read().split(',')]

print("Part 1:", end = " ")
p1 = program(A, lambda: 1, lambda x: print(x, end = " "))
p1.exec()
print("\nPart 2:", end = " ")
p2 = program(A, lambda: 5, lambda x: print(x, end = " "))
p2.exec()
