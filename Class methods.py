# class_methods.py
# Demonstrates constructor, instance variables, class variables, and @classmethod

class Student:
    # Class variable - shared by all Student objects
    school_name = "The Cooperative University of Kenya"
    total_students = 0  # Keeps track of how many students have been created

    def __init__(self, name, course):
        # Constructor - runs automatically when a new object is created
        self.name = name          # Instance variable
        self.course = course      # Instance variable
        Student.total_students += 1  # Update the class variable each time a student is created

    def display_info(self):
        """Instance method - displays this student's details."""
        print(f"{self.name} is enrolled in {self.course} at {self.school_name}")

    @classmethod
    def get_total_students(cls):
        """Class method - works with the class itself (cls), not a specific object."""
        return cls.total_students

    @classmethod
    def change_school_name(cls, new_name):
        """Class method - updates the class variable for all students."""
        cls.school_name = new_name


# Creating student objects using the constructor
s1 = Student("Simon", "Computer Science")
s2 = Student("Amina", "Information Technology")
s3 = Student("Brian", "Computer Science")

# Using instance method
s1.display_info()
s2.display_info()
s3.display_info()

# Using the class method to get total number of students created
print("\nTotal students created:", Student.get_total_students())

# Using the class method to change the class variable
Student.change_school_name("Co-op University")
print("\nAfter changing school name via class method:")
s1.display_info()