# reading input
how_to_get = {}
with open("input.txt", "r") as file:
    for line in file.read().splitlines():
        r1, p1 = line.split(" => ")
        r2 = r1.split(", ")
        r3 = [w.split(" ") for w in r2]
        r4 = [(int(w[0]), w[1]) for w in r3]
        p2 = p1.split(" ")
        p3 = (int(p2[0]), p2[1])
        how_to_get[p3[1]] = (p3[0], r4)

# returns ceil(a / b)
def ceil_div(a, b):
    return (a + b - 1) // b

def how_many_times_rec(resource):
    if resource in how_many_times_we_need_it:
        how_many_times_we_need_it[resource] += 1
    else:
        how_many_times_we_need_it[resource] = 1
    
    if resource in how_to_get and not resource in how_many_times_used:
        how_many_times_used.add(resource)
        for res in how_to_get[resource][1]:
            how_many_times_rec(res[1])

def how_much_rec(quantity, resource):
    how_many_times_we_need_it[resource] -= 1
    if resource in how_much_we_need_it:
        how_much_we_need_it[resource] += quantity
    else:
        how_much_we_need_it[resource] = quantity
        
    if how_many_times_we_need_it[resource] == 0 and resource != "ORE":
        for qua, res in how_to_get[resource][1]:
            how_much_rec(qua * ceil_div(how_much_we_need_it[resource],
                                    how_to_get[resource][0]),
                     res)

def how_much_ore(fuel):
    global how_many_times_we_need_it, how_much_we_need_it, how_many_times_used
    how_many_times_we_need_it = {}
    how_much_we_need_it = {}
    how_many_times_used = set()
    how_many_times_rec("FUEL")
    how_much_rec(fuel, "FUEL")
    return how_much_we_need_it["ORE"]

# solving Part 1
print("Part 1:", how_much_ore(1))

# solving Part 2

# finding the upper bound
high = 1
while(how_much_ore(high) <= 1000000000000):
    high *= 2

# binary search for the solution
low = 0
while high - low > 1:
    mid = (low + high) // 2
    if how_much_ore(mid) <= 1000000000000:
        low = mid
    else:
        high = mid

print("Part 2:", low)
