class StudentProfile:
    def __init__(self, student_id, name, course, experience, skills):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.experience = experience
        self.skills = skills


student_id = int(input("Enter Student ID: "))
name = input("Enter Name: ").strip()
course = input("Enter Course: ").strip()
experience = int(input("Enter Experience: "))
skills = input("Enter Skills: ").split()

student = StudentProfile(student_id, name, course, experience, skills)

skills_str = ", ".join(student.skills)
print(f"Student ID: {student.student_id}")
print(f"Name: {student.name}")
print(f"Course: {student.course}")
print(f"Experience in Years: {student.experience}")
print(f"Skills: {skills_str}")