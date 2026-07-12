# class_variables.py
# Demonstrates class variables (shared across all objects of the class)

class Student:
    # Class variable - shared by ALL instances of this class
    school_name = "The Cooperative University of Kenya"

    def __init__(self, name, course):
        # Instance variables - unique to each object
        self.name = name
        self.course = course


# Creating multiple Student objects
student1 = Student("Simon", "Computer Science")
student2 = Student("Amina", "Information Technology")

# Accessing the class variable from different objects
print("student1's school:", student1.school_name)
print("student2's school:", student2.school_name)

# Accessing the class variable directly through the class itself
print("Accessed via class directly:", Student.school_name)

# Changing the class variable affects ALL instances (unless overridden individually)
Student.school_name = "Co-op University of Kenya"
print("\nAfter changing Student.school_name:")
print("student1's school:", student1.school_name)
print("student2's school:", student2.school_name)
