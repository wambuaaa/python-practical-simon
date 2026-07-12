# float.py
# Demonstrates float variables and decimal calculations

# Creating float variables
price = 250.75
quantity = 3.5

# Calculations involving decimal numbers
total_cost = price * quantity
average = (price + quantity) / 2
difference = price - quantity

print("Price:", price)
print("Quantity:", quantity)
print("Total Cost (price * quantity):", total_cost)
print("Average (price + quantity) / 2:", average)
print("Difference (price - quantity):", difference)

# round() is useful for controlling decimal places
print("Total Cost rounded to 2 d.p.:", round(total_cost, 2))