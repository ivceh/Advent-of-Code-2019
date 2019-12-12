import sys
import os
sys.path.append(os.getcwd() + "/..")
from Intcode_computer import *

# function does not modify A
def output(A, noun, verb):
    p = program(A)
    p.A[1] = noun
    p.A[2] = verb
    p.exec()
    return p.A[0]

# reading input
with open("input.txt", "r") as file:
    A = [int(a) for a in file.read().split(',')]

# resolving Part One
print("Part One:", output(A, 12, 2))

# resolving Part Two
for noun in range(100):
    for verb in range(100):
        if output(A, noun, verb) == 19690720:
            print("Part Two A:", 100 * noun + verb)

# resolving Part Two after noticing that for my input A
#   output(A, noun, verb) == output(A, noun, 0) + verb
#   May not be correct for every input!
for noun in range(100):
    x = output(A, noun, 0)
    if x > 19690620 and x <= 19690720:
        print("Part Two B:", 100 * noun + (19690720 - x))
