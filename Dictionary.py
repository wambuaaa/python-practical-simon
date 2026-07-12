# dictionary.py
# Demonstrates dictionary creation, accessing, and updating values

# Creating a dictionary representing a student
student = {
    "name": "Simon",
    "age": 21,
    "course": "Diploma in Computer Science",
    "grade": "B+"
}

print("Student dictionary:", student)

# Accessing values
print("\nAccessing values:")
print("Name:", student["name"])
print("Age:", student.get("age"))  # get() is a safer way to access values

# Updating values
student["age"] = 22
student["grade"] = "A-"
print("\nAfter updating age and grade:", student)

# Adding a new key-value pair
student["year_of_study"] = 2
print("After adding a new key (year_of_study):", student)