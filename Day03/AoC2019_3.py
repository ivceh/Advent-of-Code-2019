import operator

# reading input
with open("input.txt", "r") as file:
    A = [(s[0], int(s[1:])) for s in file.readline().split(',')]
    B = [(s[0], int(s[1:])) for s in file.readline().split(',')]

# key: coordinates
# value: number of steps
wire1 = dict()

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

for pos, steps in go(A):
    if not pos in wire1:
        wire1[pos] = steps

inter_dists = []
inter_steps = []
for pos, steps in go(B):
    if pos in wire1:
        inter_dists.append(abs(pos[0]) + abs(pos[1]))
        inter_steps.append(wire1[pos] + steps)

print("Part One:", min(inter_dists))
print("Part Two:", min(inter_steps))
