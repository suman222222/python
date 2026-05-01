list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
result = []

for i in range(len(list1)):
    result.append(list1[i])
    result.append(list2[i])

print("Combined list:", result)
