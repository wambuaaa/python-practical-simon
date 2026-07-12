# classes.py
# Demonstrates a basic class with attributes and multiple objects

class Student:
    """A simple class representing a student."""

    def __init__(self, name, admission_number, course):
        # Instance attributes - unique to each object
        self.name = name
        self.admission_number = admission_number
        self.course = course

    def display_info(self):
        """Displays this student's information."""
        print(f"Name: {self.name}")
        print(f"Admission Number: {self.admission_number}")
        print(f"Course: {self.course}")
        print("-" * 30)


# Creating three Student objects
student1 = Student("Simon Otieno", "T006/304009/2024", "Diploma in Computer Science")
student2 = Student("Amina Hassan", "T006/304015/2024", "Diploma in Information Technology")
student3 = Student("Brian Kiptoo", "T006/304020/2024", "Diploma in Computer Science")

# Displaying their information
for student in (student1, student2, student3):
    student.display_info()