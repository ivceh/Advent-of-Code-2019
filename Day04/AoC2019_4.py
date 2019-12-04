import itertools

# read input
with open("input.txt", "r") as file:
    a, b = (int(w) for w in file.readline().split('-'))

def digits_backwards(n):
    while n > 0:
        yield n % 10
        n //= 10

# solution 1
def is_non_increasing(it):
    prev = next(it)
    for curr in it:
        if prev < curr:
            return False
        prev = curr
    return True

part1 = part2 = 0
for n in range(a, b + 1):
    grouped = [(digit, sum(1 for _ in l))
               for digit, l in itertools.groupby(digits_backwards(n))]
    rule1A = any(num >= 2 for digit, num in grouped)
    rule1B = any(num == 2 for digit, num in grouped)
    rule2 = is_non_increasing(digit for digit, num in grouped)
    if rule1A and rule2:
        part1 += 1
        if rule1B:
            part2 += 1

print("Part One", part1)
print("Part Two", part2)

#solution 2
def add_digit(n, digit):
    return n * 10 + digit

def first_non_decreasing_digit_after(a):
    digits = list(digits_backwards(a))
    n = 0
    prev_digit = 0
    digit = digits.pop()
    while digit >= prev_digit and digits:
        n = add_digit(n, digit)
        prev_digit = digit
        digit = digits.pop()
    digit = max(prev_digit, digit)
    for _ in range(len(digits) + 1):
        n = add_digit(n, digit)
    return n

def non_decreasing_digit_range(a, b):
    n = first_non_decreasing_digit_after(a)
    while n < b:
        yield n
        num_ending_nines = 0
        while n % 10 == 9:
            n //= 10
            num_ending_nines += 1
        n += 1
        new_last_digit = n % 10
        for _ in range(num_ending_nines):
            n = add_digit(n, new_last_digit)

part1 = part2 = 0
for n in non_decreasing_digit_range(a, b + 1):
    groups = [sum(1 for _ in l)
               for _, l in itertools.groupby(digits_backwards(n))]
    rule1A = any(num >= 2 for num in groups)
    rule1B = any(num == 2 for num in groups)
    if rule1A:
        part1 += 1
        if rule1B:
            part2 += 1

print("Part One", part1)
print("Part Two", part2)
