B = [
    [2, 7, 6],
    [9, 5, 1],
    [4, 3, 8]
]

n = len(B)

diag_sum = 0
above_sum = 0
below_sum = 0

max_val = B[0][0]
min_val = B[0][0]

for i in range(n):
    for j in range(n):
        value = B[i][j]

        # Diagonal
        if i == j:
            diag_sum += value

        # Above diagonal
        elif i < j:
            above_sum += value

        # Below diagonal
        else:
            below_sum += value

        # Max and Min
        if value > max_val:
            max_val = value
        if value < min_val:
            min_val = value

# Output
print("Matrix B:")
for row in B:
    print(row)

print("\nDiagonal Sum:", diag_sum)
print("Above Diagonal Sum:", above_sum)
print("Below Diagonal Sum:", below_sum)
print("Maximum Element:", max_val)
print("Minimum Element:", min_val)
