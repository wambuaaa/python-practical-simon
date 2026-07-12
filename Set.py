# set.py
# Demonstrates set creation, adding/removing elements, and automatic removal of duplicates

# Creating a set with duplicate values
numbers = {1, 2, 3, 2, 4, 1, 5}
print("Set created from duplicates {1,2,3,2,4,1,5}:", numbers)
print("Notice duplicates (2 and 1) were automatically removed")

# Adding elements
numbers.add(6)
print("\nAfter adding 6:", numbers)

# Removing elements
numbers.remove(3)  # Removes a specific element (raises error if not found)
numbers.discard(10)  # Removes if present, does nothing if not found (safer)
print("After removing 3:", numbers)

# Sets automatically ignore duplicate additions too
numbers.add(4)  # 4 already exists, so nothing changes
print("After trying to add 4 again (already exists):", numbers)