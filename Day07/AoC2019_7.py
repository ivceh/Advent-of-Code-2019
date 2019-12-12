import sys
import os
sys.path.append(os.getcwd() + "/..")
from Intcode_computer import *
import itertools
from collections import deque

# reading input
with open("input.txt", "r") as file:
    A = [int(a) for a in file.read().split(',')]

# solving Part 1
def in_func():
    global in_signal
    if in_signal:
        return in_signal.popleft()
    else:
        return 0

def out_func(x):
    global out_signal
    out_signal.append(x)

max_signal = 0
for perm in itertools.permutations([0, 1, 2, 3, 4]):
    out_signal = deque()
    for i in range(len(perm)):
        in_signal = out_signal
        in_signal.appendleft(perm[i])
        in_pos = 0
        out_signal = deque()
        p = program(A, in_func, out_func)
        p.exec()
    if(out_signal[0] > max_signal):
        max_signal = out_signal[0]
print("Part 1:", max_signal)

# solving Part 2
class program_exec_part(program):
    def exec_part(self, signal):
        if self.opcode != 99 and self.opcode == 3 and not signal:
            self.step()
        else:
            while self.opcode != 99 and (self.opcode != 3 or signal):
                self.step()

def make_in_func2(i):
    def in_func2():
        global signals, programs
        while not signals[i]:
            programs[(i + 4) % 5].exec_part(signals[(i + 4) % 5])
        return signals[i].popleft()
    return in_func2

def make_out_func2(i):
    def out_func2(x):
        global signals
        signals[(i + 1) % 5].append(x)
    return out_func2

max_signal = 0
for perm in itertools.permutations([5, 6, 7, 8, 9]):
    signals = [deque((perm[i],)) for i in range(5)]
    signals[0].append(0)
    programs = [program_exec_part(A, make_in_func2(i), make_out_func2(i))
                for i in range(5)]
    for p in programs:
        p.exec()
    if signals[0][0] > max_signal:
        max_signal = signals[0][0]
print("Part 2:", max_signal)
