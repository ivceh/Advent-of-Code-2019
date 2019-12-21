import sys
import os
sys.path.append(os.getcwd() + "/..")
from Intcode_computer import *

# reading input
with open("input.txt", "r") as file:
    A = [int(a) for a in file.read().split(",")]

def out_func(x):
    if x < 0x100:
        print(chr(x), end="")
    else:
        print(x)

def run_springdroid(s):
    global inputQ
    inputQ += [ord(c) for c in s]
    p = program(A, input_from_queue(), out_func)
    p.exec()

# solving Part 1
print("Part 1:\n")
run_springdroid("NOT J J\n"
                "AND A J\n"
                "AND B J\n"
                "AND C J\n"
                "NOT J J\n"
                "AND D J\n"
                "WALK\n")

# solving Part 2
print("\nPart 2:\n")
run_springdroid("NOT J J\n"
                "AND A J\n"
                "AND B J\n"
                "AND C J\n"
                "NOT J J\n"
                "AND D J\n"
                "OR F T\n"
                "OR I T\n"
                "AND E T\n"
                "OR H T\n"
                "AND T J\n"
                "RUN\n")