def instruction_modes(instruction):
    opcode = instruction % 100
    instruction //= 100
    mode1 = instruction % 10
    instruction //= 10
    return (opcode, mode1, instruction % 10, instruction // 10)

class program:
    def __init__(self, A, in_func = None, out_func = None):
        if isinstance(A, list):
            self.A = dict(enumerate(A))
        elif isinstance(A, dict):
            self.A = A.copy()
        else:
            raise TypeError("A must be list or dict!")
        self.pc = self.relative_base = 0
        self.in_func = in_func
        self.out_func = out_func
        self.get_opcode_modes()

    def get_opcode_modes(self):
        self.opcode, self.mode1, self.mode2, self.mode3 = instruction_modes(self.A[self.pc])

    def value_at_address(self, pc):
        if pc in self.A:
            return self.A[pc]
        else:
            return 0

    def value(self, mode, pc):
        if mode == 0:
            return self.value_at_address(self.value_at_address(pc))
        elif mode == 1:
            return self.value_at_address(pc)
        elif mode == 2:
            return self.value_at_address(self.value_at_address(pc) +
                                         self.relative_base)
        else:
            raise ValueError("Invalid mode {}!".format(mode))

    def set_value(self, mode, pc, value):
        if mode == 0:
            self.A[self.value_at_address(pc)] = value
        elif mode == 2:
            self.A[self.value_at_address(pc) + self.relative_base] = value
        else:
            raise ValueError("Invalid mode {}!".format(mode))

    def step(self):
        if self.opcode == 1:
            self.set_value(self.mode3, self.pc + 3, self.value(self.mode1, self.pc + 1) +
                                                    self.value(self.mode2, self.pc + 2))
            self.pc += 4
        elif self.opcode == 2:
            self.set_value(self.mode3, self.pc + 3, self.value(self.mode1, self.pc + 1) *
                                                    self.value(self.mode2, self.pc + 2))
            self.pc += 4
        elif self.opcode == 3:
            self.set_value(self.mode1, self.pc + 1, self.in_func())
            self.pc += 2
        elif self.opcode == 4:
            self.out_func(self.value(self.mode1, self.pc + 1))
            self.pc += 2
        elif self.opcode == 5:
            if self.value(self.mode1, self.pc + 1) == 0:
                self.pc += 3
            else:
                self.pc = self.value(self.mode2, self.pc + 2)
        elif self.opcode == 6:
            if self.value(self.mode1, self.pc + 1) == 0:
                self.pc = self.value(self.mode2, self.pc + 2)
            else:
                self.pc += 3
        elif self.opcode == 7:
            if self.value(self.mode1, self.pc + 1) < self.value(self.mode2, self.pc + 2):
                self.set_value(self.mode3, self.pc + 3, 1)
            else:
                self.set_value(self.mode3, self.pc + 3, 0)
            self.pc += 4
        elif self.opcode == 8:
            if self.value(self.mode1, self.pc + 1) == self.value(self.mode2, self.pc + 2):
                self.set_value(self.mode3, self.pc + 3, 1)
            else:
                self.set_value(self.mode3, self.pc + 3, 0)
            self.pc += 4
        elif self.opcode == 9:
            self.relative_base += self.value(self.mode1, self.pc + 1)
            self.pc += 2
        else:
            raise ValueError("Invalid opcode {}!".format(self.opcode))
        self.get_opcode_modes()

    def exec(self):
        while self.opcode != 99:
            self.step()

    def exec_until_input(self):
        while self.opcode != 99 and self.opcode != 3:
            self.step()
