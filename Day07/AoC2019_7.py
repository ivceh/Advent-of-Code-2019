import itertools
from collections import deque

def instruction_modes(instruction):
    opcode = instruction % 100
    instruction //= 100
    mode1 = instruction % 10
    instruction //= 10
    return (opcode, mode1, instruction % 10, instruction // 10)

def value(A, mode, pc):
    if mode == 0:
        return A[A[pc]]
    elif mode == 1:
        return A[pc]
    else:
        raise ValueError("Invalid mode!")

class program:
    def __init__(self, A, in_func, out_func):
        self.A = A.copy()
        self.pc = 0
        self.in_func = in_func
        self.out_func = out_func
        self.get_opcode_modes()

    def get_opcode_modes(self):
        self.opcode, self.mode1, self.mode2, self.mode3 = instruction_modes(self.A[self.pc])

    def step(self):
        if self.opcode == 1:
            self.A[self.A[self.pc + 3]] = value(self.A, self.mode1, self.pc + 1) + \
                                          value(self.A, self.mode2, self.pc + 2)
            self.pc += 4
        elif self.opcode == 2:
            self.A[self.A[self.pc + 3]] = value(self.A, self.mode1, self.pc + 1) * \
                                          value(self.A, self.mode2, self.pc + 2)
            self.pc += 4
        elif self.opcode == 3:
            self.A[self.A[self.pc + 1]] = self.in_func()
            self.pc += 2
        elif self.opcode == 4:
            self.out_func(value(self.A, self.mode1, self.pc + 1))
            self.pc += 2
        elif self.opcode == 5:
            if value(self.A, self.mode1, self.pc + 1) == 0:
                self.pc += 3
            else:
                self.pc = value(self.A, self.mode2, self.pc + 2)
        elif self.opcode == 6:
            if value(self.A, self.mode1, self.pc + 1) == 0:
                self.pc = value(self.A, self.mode2, self.pc + 2)
            else:
                self.pc += 3
        elif self.opcode == 7:
            if value(self.A, self.mode1, self.pc + 1) < value(self.A, self.mode2, self.pc + 2):
                self.A[self.A[self.pc + 3]] = True
            else:
                self.A[self.A[self.pc + 3]] = False
            self.pc += 4
        elif self.opcode == 8:
            if value(self.A, self.mode1, self.pc + 1) == value(self.A, self.mode2, self.pc + 2):
                self.A[self.A[self.pc + 3]] = True
            else:
                self.A[self.A[self.pc + 3]] = False
            self.pc += 4
        else:
            raise ValueError("Invalid opcode {}!".format(self.opcode))
        self.get_opcode_modes()

    def exec(self):
        while self.opcode != 99:
            self.step()

    def exec_part(self, signal):
        if self.opcode != 99 and self.opcode == 3 and not signal:
            self.step()
        else:
            while self.opcode != 99 and (self.opcode != 3 or signal):
                self.step()

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
    programs = [program(A, make_in_func2(i), make_out_func2(i))
                for i in range(5)]
    for p in programs:
        p.exec()
    if signals[0][0] > max_signal:
        max_signal = signals[0][0]
print("Part 2:", max_signal)
