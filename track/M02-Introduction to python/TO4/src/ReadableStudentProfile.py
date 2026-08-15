class StudentProfile:
    def __init__(self, student_id, name, course, experience, skills):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.experience = experience
        self.skills = skills

    def __str__(self):
        skills_str = ", ".join(self.skills)
        return (
            f"STUDENT PROFILE\n"
            f"Student ID: {self.student_id}\n"
            f"Name: {self.name}\n"
            f"Course: {self.course}\n"
            f"Experience in Years: {self.experience}\n"
            f"Skills: {skills_str}"
        )

# Read input data
student_id = int(input("Enter the Student ID: "))
name = input("Enter the Name:").strip()
course = input("Enter the Course:").strip()
experience = int(input("Enter the Experience in Years:").strip())
skills = input("Enter the Skills:").strip().split()

# Create object and print profile
student = StudentProfile(student_id, name, course, experience, skills)
print(student)
