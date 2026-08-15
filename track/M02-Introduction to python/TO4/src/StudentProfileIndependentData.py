class StudentProfile:
    def __init__(self, student_id, name, course):
        self.student_id = student_id
        self.name = name
        self.course = course


# Read input for the first student
first_id = int(input("Enter student 1 ID: "))
first_name = input("Enter student 1 name: ").strip()
first_course = input("Enter student 1 course: ").strip()

# Read input for the second student
second_id = int(input("Enter student 2 ID: "))
second_name = input("Enter student 2 name: ").strip()
second_course = input("Enter student 2 course: ").strip()

# Create two separate StudentProfile objects
student1 = StudentProfile(first_id, first_name, first_course)
student2 = StudentProfile(second_id, second_name, second_course)

# Print the first student's data
print("\nStudent 1")
print(f"ID: {student1.student_id}")
print(f"Name: {student1.name}")
print(f"Course: {student1.course}")

# Print the second student's data
print("\nStudent 2")
print(f"ID: {student2.student_id}")
print(f"Name: {student2.name}")
print(f"Course: {student2.course}")