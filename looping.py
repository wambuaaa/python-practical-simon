# looping.py
# Demonstrates for loops and while loops

# 1. for loop - print numbers from 1 to 20
print("Numbers from 1 to 20:")
for i in range(1, 21):
    print(i, end=" ")
print()

# 2. for loop - multiplication table of a number entered by the user
num = int(input("\nEnter a number to see its multiplication table: "))
print(f"Multiplication table of {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# 3. while loop - sum of numbers from 1 to 100
total = 0
count = 1
while count <= 100:
    total += count
    count += 1
print("\nSum of numbers from 1 to 100:", total)

# 4. Print only the even numbers between 1 and 50
print("\nEven numbers between 1 and 50:")
for i in range(1, 51):
    if i % 2 == 0:
        print(i, end=" ")
print()
