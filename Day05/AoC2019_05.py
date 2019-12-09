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

# reading input
with open("input.txt", "r") as file:
    A = [int(a) for a in file.read().split(',')]

print("Part 1:", end = " ")
p1 = program(A, lambda: 1, lambda x: print(x, end = " "))
p1.exec()
print("\nPart 2:", end = " ")
p2 = program(A, lambda: 5, lambda x: print(x, end = " "))
p2.exec()
