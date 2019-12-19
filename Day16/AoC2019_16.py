# reading input
with open("input.txt", "r") as file:
    A = [int(a) for a in file.read()]

# solving Part 1 using cumulative sum
def phase(A):
    sumA = [0]
    s = 0
    for a in A:
        s += a
        sumA.append(s)

    B = []
    for i in range(1, len(A) + 1):
        pow = 1
        s = 0
        for j in range(i - 1, len(A) + 1, 2 * i):
            s += pow * (sumA[min(len(A), j + i)] - sumA[j])
            pow *= -1
        B.append(abs(s) % 10)
    return B

def fft(A, phases):
    for _ in range(phases):
        A = phase(A)
    return A

B = fft(A, 100)
print("Part 1:", end = " ")
for d in B[:8]:
    print(d, end = "")

# solving Part 2
# Number of digits to skip for me was 5973847 of 6500000
# For signal S if n > len(S) / 2 we can show that:
# fft(S, k)[n] = sum(binomial(k + i - 1, k - 1) * S[n + i]
#                    for i in range(len(S) - n))
n = 0
for b in A[:7]:
    n *= 10
    n += b

def element10000(A, i):
    return A[i % len(A)]

print("\nPart 2:", end = " ")
for i in range(n, n + 8):
    s = 0
    binomial = 1
    for j in range(len(A) * 10000 - i):
        s += binomial * element10000(A, i + j)
        s %= 10
        binomial *= j + 100
        binomial //= j + 1
    print(s, end = "")
