import operator

# reading input
with open("input.txt", "r") as file:
    A = [(s[0], int(s[1:])) for s in file.readline().split(',')]
    B = [(s[0], int(s[1:])) for s in file.readline().split(',')]

def step(direction):
    global pos, steps
    steps += 1
    if direction == 'U':
        pos = (pos[0], pos[1] - 1)
    elif direction == 'D':
        pos = (pos[0], pos[1] + 1)
    elif direction == 'L':
        pos = (pos[0] - 1, pos[1])
    elif direction == 'R':
        pos = (pos[0] + 1, pos[1])
    else:
        raise InvalidArgument("Unknown direction!")

# key: coordinates
# value: ('A' for first wire or 'B' for second wire or 'X' for intersection,
#         number of steps)
wire1 = dict()

def go(wire):
    global pos, steps
    pos = (0, 0)
    steps = 0
    for move in wire:
        for i in range(move[1]):
            step(move[0])
            yield

for _ in go(A):
    if not pos in wire1:
        wire1[pos] = steps

inter_dists = []
inter_steps = []
for _ in go(B):
    if pos in wire1:
        inter_dists.append(abs(pos[0]) + abs(pos[1]))
        inter_steps.append(wire1[pos] + steps)

print("Part One:", min(inter_dists))
print("Part Two:", min(inter_steps))
