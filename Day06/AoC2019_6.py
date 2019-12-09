# key: object
# value: set of objects in its orbit
orbits = dict()

# key: object
# value: object in which it orbits
parents = dict()

# reading input, creating tree structure
with open("input.txt", "r") as file:
    for line in file.read().splitlines():
        try:
            a, b = line.split(')')
        except:
            print(line)
        
        if a in orbits:
            orbits[a].add(b)
        else:
            orbits[a] = {b}
        parents[b] = a

# finding the root (the object which orbits nothing)
while a in parents:
    a = parents[a]

# Solving Part 1
# argument: object
# return value: (number of objects in its direct and indirect orbits,
#                total number of orbits under it)
def rec1(obj):
    if obj in orbits:
        suma = sumb = 0
        for child in orbits[obj]:
            a, b = rec1(child)
            suma += a + 1
            sumb += b
        return (suma, suma + sumb)
    else:
        return (0, 0)

print("Part 1:", rec1(a)[1])

# Solving Part 2
# arguments: objects a, b and obj
# return value: None if neither a nor b are in object's
#                    direct or indirect orbit,
#               distance between obj and a if a is in object's
#                    direct or indirect orbit,
#               distance between obj and b if b is in object's
#                    direct or indirect orbit,
#               (distance between a and b,) if a and b are both
#                    in object's direct or indirect orbit
def rec2(a, b, obj):
    if obj == a:
        return 0
    if obj == b:
        return 0
    if obj in orbits:
        l = [rec2(a, b, child) for child in orbits[obj]]
        notNone = [el for el in l if el != None]
        if len(notNone) == 0:
            return None
        elif len(notNone) == 1:
            if isinstance(notNone[0], int):
                return 1 + notNone[0]
            else:
                return notNone[0]
        else:
            return (2 + notNone[0] + notNone[1],)
    else:
        return None

print("Part 2:", rec2(parents["YOU"], parents["SAN"], a)[0])
