a = ['a', 'a', 'b', 'c', 'c', 'd', 'c', 'e', 'd', 'e']

unique = []

# Remove duplicates
for item in a:
    if item not in unique:
        unique.append(item)

# Sort in descending order
for i in range(len(unique)):
    for j in range(0, len(unique) - i - 1):
        if unique[j] < unique[j + 1]:
            unique[j], unique[j + 1] = unique[j + 1], unique[j]

print(unique)
