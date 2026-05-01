# Addition
list1 = [1, 2, 3, 4, 5, 6]
list2 = [1, 2, 3, 4, 5, 6]
result = []

for i in range(len(list1)):
    result.append(list1[i] + list2[i])

print("Addition result:", result)


# Concatenation
a = ['a', 'b', 'c', 'd', 'e']
b = ['f', 'g', 'h', 'i', 'j']
result2 = []

for i in range(len(a)):
    result2.append(a[i] + b[i])

print("Concatenation result:", result2)
