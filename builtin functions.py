# builtin_functions.py
# Demonstrates the use of at least 10 built-in Python functions

numbers = [4, 8, 15, 16, 23, 42]
text = "Cooperative University"

print("List used:", numbers)
print("String used:", text)

# 1. len() - returns the number of items
print("\nlen(numbers):", len(numbers))

# 2. max() - returns the largest item
print("max(numbers):", max(numbers))

# 3. min() - returns the smallest item
print("min(numbers):", min(numbers))

# 4. sum() - adds up all items
print("sum(numbers):", sum(numbers))

# 5. type() - returns the data type of an object
print("type(numbers):", type(numbers))

# 6. sorted() - returns a new sorted list
print("sorted(numbers, reverse=True):", sorted(numbers, reverse=True))

# 7. abs() - returns the absolute value
print("abs(-25):", abs(-25))

# 8. round() - rounds a number to a given precision
print("round(3.14159, 2):", round(3.14159, 2))

# 9. print() - displays output (used throughout this file)

# 10. input() - takes user input (returns a string)
name = input("\nEnter your name to demonstrate input(): ")
print("Hello,", name)

# Bonus: str(), int(), float() - type conversion functions
print("\nint('10') + 5 =", int("10") + 5)
print("str(100) has type:", type(str(100)))
