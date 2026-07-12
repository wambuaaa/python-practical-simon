# lambda_functions.py
# Demonstrates lambda (anonymous) functions

# 1. Lambda function to add two numbers
add = lambda a, b: a + b
print("add(3, 4):", add(3, 4))

# 2. Lambda function to multiply two numbers
multiply = lambda a, b: a * b
print("multiply(3, 4):", multiply(3, 4))

# 3. Using a lambda function to sort a list of tuples by the second value
students = [("Amina", 78), ("Brian", 65), ("Cynthia", 91)]
sorted_students = sorted(students, key=lambda student: student[1])
print("\nStudents sorted by score (ascending):", sorted_students)

# 4. Using filter() with a lambda function - keep only even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda n: n % 2 == 0, numbers))
print("\nEven numbers filtered from", numbers, ":", even_numbers)

# 5. Using map() with a lambda function - square each number
squared_numbers = list(map(lambda n: n ** 2, numbers))
print("Squares of", numbers, ":", squared_numbers)