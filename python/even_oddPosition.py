# Even positions
a = [43, 23, 21, 44, 56, 75]
result = []

for i in range(len(a)):
    if i % 2 != 0:
        result.append(a[i])

print("Even position elements:", result)


# Odd positions
b = [12, 22, 32, 42, 52, 62]
result2 = []

for i in range(len(b)):
    if i % 2 == 0:
        result2.append(b[i])

print("Odd position elements:", result2)
