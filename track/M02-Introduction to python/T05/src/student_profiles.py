class StudentProfile:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def display_profile(self):
        print(f"{self.category}: {self.name}")

class FresherStudent(StudentProfile):
    pass

class ExperiencedStudent(StudentProfile):
    pass

fresher_name = input().strip()
experienced_name = input().strip()

fresher = FresherStudent(fresher_name, "Fresher Student")
experienced = ExperiencedStudent(experienced_name, "Experienced Student")

fresher.display_profile()
experienced.display_profile()