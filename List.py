# list.py
# Demonstrates list creation, adding/removing/updating items, and looping

# Creating a list
fruits = ["apple", "banana", "mango"]
print("Original list:", fruits)

# Adding items
fruits.append("orange")       # Adds to the end
fruits.insert(1, "grape")     # Inserts at a specific position
print("After adding items:", fruits)

# Removing items
fruits.remove("banana")       # Removes a specific item
popped_item = fruits.pop()    # Removes and returns the last item
print("After removing items:", fruits)
print("Item removed with pop():", popped_item)

# Updating an item
fruits[0] = "green apple"
print("After updating first item:", fruits)

# Looping through the list
print("\nLooping through the list:")
for fruit in fruits:
    print("-", fruit)