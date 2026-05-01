#Store student data in a 2D list and
# Calculate average marks for each student

# 2D list: [Name, Math, Science, English, Physics, Computer]

a = [
    ["John", 88, 86, 81, 66, 76],
    ["Sam", 77, 74, 73, 64, 70],
    ["Anna", 71, 74, 73, 78, 80],
    ["Ben", 76, 64, 54, 67, 78],
    ["Jeff", 90, 80, 79, 86, 75]
]

for i in range(len(a)):
    total=0
    for j in range(1,len(a[i])):
        total+=a[i][j]
    average=total/(len(a[i])-1)
