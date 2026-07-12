# string.py
# Demonstrates string creation, concatenation, indexing, slicing, and methods

# Creating strings
first_name = "Simon"
last_name = "Otieno"

# Concatenation - joining strings together
full_name = first_name + " " + last_name
print("Full Name (concatenation):", full_name)

# Indexing - accessing individual characters (starts at 0)
print("\nIndexing on full_name:")
print("First character:", full_name[0])
print("Last character:", full_name[-1])

# Slicing - extracting a portion of a string [start:stop]
print("\nSlicing on full_name:")
print("First 5 characters:", full_name[0:5])
print("Characters from index 6 to end:", full_name[6:])

# String methods
sentence = "python is Fun to Learn"
print("\nOriginal sentence:", sentence)
print("upper():", sentence.upper())          # Converts to uppercase
print("lower():", sentence.lower())           # Converts to lowercase
print("replace():", sentence.replace("Fun", "Exciting"))  # Replaces a substring
print("split():", sentence.split())           # Splits string into a list of words
