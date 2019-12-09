# reading input
with open("input.txt", "r") as file:
    image = file.read()

# solving Part 1
minzeros = 151
for i in range(len(image) // 150):
    layer = image[150 * i : 150 * (i + 1)]
    zeros = sum(1 for p in layer if p == '0')
    ones = sum(1 for p in layer if p == '1')
    twos = sum(1 for p in layer if p == '2')
    if zeros < minzeros:
        minzeros = zeros
        part1 = ones * twos
print("Part 1:", part1)

# solving Part 2
print("Part 2:")
for i in range(6):
    for j in range(25):
        for k in range(len(image) // 150):
            if image[150 * k + 25 * i + j] != '2':
                if image[150 * k + 25 * i + j] == '1':
                    print('#', end = '')
                else:
                    print(' ', end = '')
                break
    print()
    


    
