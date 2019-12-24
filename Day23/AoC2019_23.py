import sys
import os
sys.path.append(os.getcwd() + "/..")
from Intcode_computer import *
from abc import ABC, abstractmethod
from enum import IntEnum

# reading input
with open("input.txt", "r") as file:
    A = [int(a) for a in file.read().split(",")]

class State(IntEnum):
    stateDestination = 0
    stateX = 1
    stateY = 2

def next_state(s):
    return State((s + 1) % 3)

class SolutionFound(Exception):
    pass

class NIC(program, ABC):
    def __init__(self, A, i):
        self.state = State.stateDestination
        self.inputQ = deque([i])
        self.network_address = i

        def in_func():
            if self.inputQ:
                return self.inputQ.popleft()
            else:
                return self.inputQ_empty()

        def out_func(x):
            if self.state == State.stateDestination:
                self.outputQindex = x
            elif self.state == State.stateX:
                self.outputX = x
            elif self.state == State.stateY:
                if self.outputQindex < len(nics):
                    nics[self.outputQindex].inputQ += [self.outputX, x]
                    self.note()
                elif self.outputQindex == 255:
                    self.output_to_255(x)
                else:
                    raise ValueError("Unknown destination address!")
            self.state = next_state(self.state)

        program.__init__(self, A, in_func, out_func)
        ABC.__init__(self)

    @abstractmethod
    def inputQ_empty(self):
        pass

    @abstractmethod
    def output_to_255(self, x):
        pass

    def note(self):
        pass

def exec_all(NIC_class):
    global nics
    try:
        nics = [NIC_class(A, i) for i in range(50)]
        while not all(p.finished() for p in nics):
            for p in nics:
                if not p.finished():
                    p.step()
                p.exec_until_input()
    except SolutionFound:
        pass

# solving Part 1
class NIC1(NIC):
    def inputQ_empty(self):
        return -1

    def output_to_255(self, x):
        print(x)
        raise SolutionFound

print("Part 1:", end = " ")
exec_all(NIC1)

# solving Part 2
class NIC2(NIC):
    def inputQ_empty(self):
        global lastY
        idleNICs.add(self.network_address)
        if len(idleNICs) == 50:
            nics[0].inputQ += NATpacket
            if lastY == NATpacket[1]:
                print(NATpacket[1])
                raise SolutionFound
            else:
                lastY = NATpacket[1]
            idleNICs.discard(0)
        return -1

    def output_to_255(self, x):
        global NATpacket
        NATpacket = (self.outputX, x)

    def note(self):
        idleNICs.discard(self.outputQindex)

idleNICs = set()
lastY = None
print("Part 2:", end = " ")
exec_all(NIC2)