# Program to calculate area and perimeter of a rectangle

# Taking input from the user
length = float(input("Enter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))

# Calculating area
area = length * breadth   # Formula: l × b

# Calculating perimeter
perimeter = 2 * (length + breadth)   # Formula: 2(l + b)

# Displaying results
print("Area =", area)
print("Perimeter =", perimeter)
