with open("input.txt", "r") as file:
    A = [int(l) for l in file.read().splitlines()]

# resolving Part One
print("Part One:", sum(n // 3 - 2 for n in A))

# resolving Part Two
s = 0
for n in A:
    x = n // 3 - 2
    while x > 0:
        s += x
        x //= 3
        x -= 2

print("Part Two:", s)
