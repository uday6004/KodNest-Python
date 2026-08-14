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

    def filter_students_by_course(self, required_course):
        matching_students = []
        required_course = required_course.lower()

        for student in self.student_profiles:
            if student.course.lower() == required_course:
                matching_students.append(student)

        return matching_students


manager = PlacementManager()

n = int(input("Number of students: "))

for _ in range(n):
    student_id = int(input("Enter student ID: "))
    name = input("Enter name: ").strip()
    course = input("Enter course: ").strip()

    student = StudentProfile(student_id, name, course)
    manager.add_student_profile(student)

filter_course = input().strip()

result = manager.filter_students_by_course(filter_course)

if result:
    for student in result:
        print(student)
else:
    print(f"No students found for course: {filter_course}")
