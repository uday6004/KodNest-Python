class StudentProfile:
    def show_profile(self):
        pass


class FresherStudent(StudentProfile):
    def __init__(self, name, graduation_year):
        self.name = name
        self.graduation_year = graduation_year

    def show_profile(self):
        print(f"{self.name} - Fresher - Graduation Year: {self.graduation_year}")


class ExperiencedStudent(StudentProfile):
    def __init__(self, name, experience):
        self.name = name
        self.experience = experience

    def show_profile(self):
        print(f"{self.name} - Experienced - Experience: {self.experience} years")


fresher_name = input("Enter the name of the fresher student: ")
graduation_year = int(input("Enter the graduation year of the fresher student: "))
experienced_name = input("Enter the name of the experienced student: ")
experience = int(input("Enter the experience of the experienced student: "))

students = [
    FresherStudent(fresher_name, graduation_year),
    ExperiencedStudent(experienced_name, experience)
]

for student in students:
    student.show_profile()