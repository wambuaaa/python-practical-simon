# boolean.py
# Demonstrates Boolean variables and comparison operators

# Creating Boolean variables
is_student = True
is_graduated = False

print("is_student:", is_student)
print("is_graduated:", is_graduated)

# Comparison operators
x = 10
y = 20

print("\nComparison operators using x =", x, "and y =", y)
print("x == y:", x == y)   # Equal to
print("x != y:", x != y)   # Not equal to
print("x > y:", x > y)     # Greater than
print("x < y:", x < y)     # Less than
print("x >= y:", x >= y)   # Greater than or equal to
print("x <= y:", x <= y)   # Less than or equal to

# Comparison operators return Boolean values
result = x < y
print("\nResult of (x < y) is a boolean:", result, "| type:", type(result))
