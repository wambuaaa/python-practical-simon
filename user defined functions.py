# user_defined_functions.py
# Demonstrates user-defined functions

# 1. Function to add two numbers
def add_numbers(a, b):
    """Returns the sum of two numbers."""
    return a + b

# 2. Function to find the area of a rectangle
def rectangle_area(length, width):
    """Returns the area of a rectangle given its length and width."""
    return length * width

# 3. Function to determine whether a number is prime
def is_prime(n):
    """Returns True if n is a prime number, otherwise False."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# 4. Function to find the factorial of a number
def factorial(n):
    """Returns the factorial of n (n!)."""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# 5. Function to display a student's details
def display_student(name, admission_no, course):
    """Prints out a student's details."""
    print(f"Name: {name}")
    print(f"Admission No: {admission_no}")
    print(f"Course: {course}")

# --- Testing the functions ---
print("add_numbers(5, 7):", add_numbers(5, 7))
print("rectangle_area(4, 6):", rectangle_area(4, 6))
print("is_prime(17):", is_prime(17))
print("is_prime(18):", is_prime(18))
print("factorial(5):", factorial(5))

print("\nStudent details:")
display_student("Simon", "T006/304009/2024", "Diploma in Computer Science")
