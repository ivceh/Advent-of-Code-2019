def same_direction(d1, d2):
    return d1[0] * d2[1] == d1[1] * d2[0] and (d1[0] * d2[0] > 0 or
                                               d1[1] * d2[1] > 0)

# reading input
with open("input.txt", "r") as file:
    A = file.read().splitlines()

# solving Part 1
max_visible = 0
for i, row in enumerate(A):
    for j, point in enumerate(row):
        if point == "#":
            # list of directions of asteroids visible from (j, i)
            directions = []
            for k, row2 in enumerate(A):
                for l, point2 in enumerate(row2):
                    if point2 == "#" and (k != i or l != j):
                        d = (l - j, k - i)
                        same_direction_found = any(same_direction(d, d2)
                                                   for d2 in directions)
                        if not same_direction_found:
                            directions.append(d)
            if len(directions) > max_visible:
                max_visible = len(directions)
                max_directions = directions
                max_point = (j, i)
print("Part 1:", max_visible)

# solving Part 2

# input: direction vector
# output: (quadrant, value to sort directions in the same quadrant)
def sort_key(d):
    dx, dy = d
    if dx >= 0 and dy < 0:
        return (1, dx / dy)
    elif dx > 0 and dy >= 0:
        return (2, dy / dx)
    elif dx <= 0 and dy > 0:
        return (3, dx / dy)
    elif dx < 0 and dy <= 0:
        return (4, dy / dx)
    else:
        raise ValueError("Direction vector " + str(d))

# finding 200th direction
l = list(max_directions)
l.sort(key = sort_key)
dir200 = l[199]

# finding the closest point in that direction
min_dist_sqr = len(A) ** 2 + len(A[0]) ** 2
for i, row in enumerate(A):
    for j, point in enumerate(row):
        if point == "#":
            d = (j - max_point[0], i - max_point[1])
            if same_direction(d, dir200):
                dist_sqr = d[0] ** 2 + d[1] ** 2
                if dist_sqr < min_dist_sqr:
                    min_dist_sqr = dist_sqr
                    point2 = (j, i)

print("Part 2:", point2[0] * 100 + point2[1])

