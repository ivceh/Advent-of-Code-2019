import sys
import os
sys.path.append(os.getcwd() + "/..")
from collections import namedtuple

# reading input
with open("input.txt", "r") as file:
    A = file.read().splitlines()

# everything is calculated in modular arithmetic mod N

# linear function f(x) = a * x + b
class Linear(namedtuple("Linear", ("a", "b"))):
    # identity function f(x) = x
    @staticmethod
    def identity():
        return Linear(1, 0)

    # composition (f * g)(x) = f(g(x))
    def __mul__(self, other):
        return Linear(self.a * other.a % N, (self.a * other.b + self.b) % N)

    # apply function to number f[x] = a * x + b
    def __getitem__(self, arg):
        return (self.a * arg + self.b) % N

    # returns inverse of linear function using modular inverse calculation
    @staticmethod
    def inv(f):
        mod_inv_a = pow(f.a, -1, N)
        return Linear(mod_inv_a, (-mod_inv_a * f.b) % N)

    # n-th power of the operator (compose operator with itself n times)
    # exponentiation by squaring algorithm is used
    def __pow__(self, n):
        if n < 0:
            return Linear.inv(self) ** (-n)
        else:
            temp = self
            retval = Linear.identity()
            while n > 0:
                if n % 2 == 1:
                    retval *= temp
                temp *= temp
                n //= 2
            return retval

# Shuffling is represented as linear function in modukar arithmetic mod N.
# If f(i) == j, that means that card on i-th position after shuffling
#               was on j-th position before shuffling
# If (f ** -1)[i] == j, that means that card on i-th position before shuffling
#                       is on j-th position after shuffling

def shuffling_from_line(line):
    words = line.split(" ")
    if words[1] == "into":    # deal into new stack
        return Linear(-1, -1)
    elif words[0] == "cut":   # cut N cards
        return Linear(1, -int(words[1]))
    elif words[1] == "with":  # deal with increment N
        return Linear(int(words[3]), 0)
    else:
        raise ValueError("Unknown shuffling technique!")

def shuffling_from_input(A):
    retval = Linear.identity()
    for line in A:
        retval = shuffling_from_line(line) * retval
    return retval

# solving Part 1
N = 10007
S = shuffling_from_input(A)
print("Part 1:", S[2019])

# solving Part 2
N = 119315717514047
S = shuffling_from_input(A) ** -101741582076661
print("Part 2:", S[2020])