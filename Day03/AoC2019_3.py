# read input
with open("input.txt", "r") as file:
    A = [(s[0], int(s[1:])) for s in file.readline().split(',')]
    B = [(s[0], int(s[1:])) for s in file.readline().split(',')]

# goes through coordinates of the wire
def go(wire):
    x = y = steps = 0
    for move in wire:
        for i in range(move[1]):
            if move[0] == 'U':
                y -= 1
            elif move[0] == 'D':
                y += 1
            elif move[0] == 'L':
                x -= 1
            elif move[0] == 'R':
                x += 1
            else:
                raise ValueError("Unknown direction!")
            steps += 1
            yield ((x, y), steps)

# key: coordinates of the first wire
# value: number of steps
wireA = dict()

# fill wireA dictionary
for pos, steps in go(A):
    if not pos in wireA:
        wireA[pos] = steps

# check for intersection between wires
inter_dists = []
inter_steps = []
for pos, steps in go(B):
    if pos in wireA:
        inter_dists.append(abs(pos[0]) + abs(pos[1]))
        inter_steps.append(wireA[pos] + steps)

# output
print("Part One:", min(inter_dists))
print("Part Two:", min(inter_steps))
