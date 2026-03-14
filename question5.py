 # Program to compute the expression:
# x^3 + 3x^2y + 3xy^2 + y^3

# Taking input values from user
x = float(input("Enter value of x: "))
y = float(input("Enter value of y: "))

# Calculating the expression
result = x**3 + 3*(x**2)*y + 3*x*(y**2) + y**3

# Displaying the result
print("Result =", result)
