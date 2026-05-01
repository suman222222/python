m = int(input("Enter number of rows: "))
n = int(input("Enter number of columns: "))

matrix = []

for i in range(m):
    row = []
    for j in range(n):
        if i == j:
            row.append(1)
        elif i < j:
            row.append(2)
        else:
            row.append(-2)
    matrix.append(row)

# Display the matrix
print("\nMatrix:")
for row in matrix:
    print(row)
      
