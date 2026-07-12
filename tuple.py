# tuple.py
# Demonstrates tuple creation, indexing, and immutability

# Creating a tuple
coordinates = (6.1622, 1.2921, "Nairobi")
print("Tuple:", coordinates)

# Accessing elements by index
print("First element (latitude):", coordinates[0])
print("Second element (longitude):", coordinates[1])
print("Third element (city):", coordinates[2])

# Tuples cannot be modified after creation (they are immutable).
# Uncommenting the line below would raise:
# TypeError: 'tuple' object does not support item assignment
#
# coordinates[0] = 0.0

# Instead, if you need a "changed" version, you must create a new tuple
new_coordinates = (0.0, 1.2921, "Nairobi")
print("New tuple (original unchanged):", new_coordinates)
print("Original tuple is still:", coordinates)
