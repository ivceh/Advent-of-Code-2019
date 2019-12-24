# reading input
with open("input.txt", "r") as file:
    A = [list(line) for line in file.read().splitlines()]

# bugs are represented as set of positions
def next_state(bugs, adjacent):
    adjacent_bugs = {}
    for bug in bugs:
        for pos in adjacent(bug):
            if pos in adjacent_bugs:
                adjacent_bugs[pos] += 1
            else:
                adjacent_bugs[pos] = 1
    bugs2 = set()
    for pos, val in adjacent_bugs.items():
        if pos in bugs:
            if val == 1:
                bugs2.add(pos)
        else:
            if val in (1, 2):
                bugs2.add(pos)
    return bugs2

# solving Part 1
def adjacent1(pos):
    i, j = pos
    for i2, j2 in ((i - 1, j), (i + 1 , j), (i, j - 1), (i, j + 1)):
        if 0 <= i2 < 5 and 0 <= j2 < 5:
            yield i2, j2

def biodiversity(bugs):
    return sum(2 ** (5 * i + j) for i, j in bugs)

states = set()
bugs = {(i, j) for i in range(5) for j in range(5) if A[i][j] == "#"}
while frozenset(bugs) not in states:
    states.add(frozenset(bugs))
    bugs = next_state(bugs, adjacent1)
print("Part 1:", biodiversity(bugs))

# solving Part 2
def adjacent2(tile):
    depth, i, j = tile
    for i2, j2 in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
        if i2 < 0:
            yield depth - 1, 1, 2
        elif i2 >= 5:
            yield depth - 1, 3, 2
        elif j2 < 0:
            yield depth - 1, 2, 1
        elif j2 >= 5:
            yield depth - 1, 2, 3
        elif i2 == j2 == 2:
            if i == 1:
                for k in range(5):
                    yield depth + 1, 0, k
            elif i == 3:
                for k in range(5):
                    yield depth + 1, 4, k
            elif j == 1:
                for k in range(5):
                    yield depth + 1, k, 0
            elif j == 3:
                for k in range(5):
                    yield depth + 1, k, 4
            else:
                raise ValueError("This should not happen!")
        else:
            yield depth, i2, j2

def after_n_minutes(bugs, n, adjacent):
    for i in range(n):
        bugs = next_state(bugs, adjacent)
    return bugs

bugs = {(0, i, j) for i in range(5) for j in range(5) if A[i][j] == "#"}
print("Part 2:", len(after_n_minutes(bugs, 200, adjacent2)))
