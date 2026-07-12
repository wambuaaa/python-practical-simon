# selection.py
# Demonstrates if, if...else, and if...elif...else statements

# 1. Simple if statement
age = 20
if age >= 18:
    print("You are an adult.")

# 2. if...else - determine pass or fail based on score
score = 65
if score >= 50:
    print("\nResult: You PASSED with a score of", score)
else:
    print("\nResult: You FAILED with a score of", score)

# 3. if...elif...else - check whether a number is even or odd
number = int(input("\nEnter a number to check if it's even or odd: "))
if number % 2 == 0:
    print(number, "is EVEN")
else:
    print(number, "is ODD")

# 4. if...elif...else - find the largest of three numbers
num1, num2, num3 = 12, 45, 30
if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3
print("\nAmong", num1, ",", num2, "and", num3, "the largest is:", largest)
