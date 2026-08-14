class StudentProfile:
    def __init__(self, student_id, name, course):
        self.student_id = student_id
        self.name = name
        self.course = course

    def __str__(self):
        return f"{self.student_id} - {self.name} - {self.course}"


class PlacementManager:
    def __init__(self):
        self.student_profiles = []

    def add_student_profile(self, student_profile):
        self.student_profiles.append(student_profile)

    def find_student_by_id(self, student_id):
        for student_profile in self.student_profiles:
            if student_profile.student_id == student_id:
                return student_profile
        return None


manager = PlacementManager()

n = int(input("Enter Number of students:"))

for _ in range(n):
    student_id = int(input("enter student id:"))
    name = input("Enter name: ")
    course = input("Enter course: ")

    student = StudentProfile(student_id, name, course)
    manager.add_student_profile(student)

required_id = int(input("Enter student ID to search: "))
result = manager.find_student_by_id(required_id)

if result is not None:
    print(result)
else:
    print(f"Student profile with ID {required_id} not found")