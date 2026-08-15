class StudentProfile:
    def __init__(self, name, experience, skills):
        self.name = name
        self.experience = experience
        self.skills = skills

    def update_experience(self, new_experience):
        self.experience = new_experience

    def add_skill(self, new_skill):
        self.skills.append(new_skill)

# Read initial inputs
name = input("Enter the name:").strip()
experience = int(input("Enter the experience:").strip())
skills = input("Enter the Skills: ").strip().split()

# Create instance
student = StudentProfile(name, experience, skills)

# Read update inputs
new_experience = int(input("Enter the new experience:").strip())
new_skill = input("Enter the new skill:").strip()

# Call update methods
student.update_experience(new_experience)
student.add_skill(new_skill)

# Output results
print(f"Name: {student.name}")
print(f"Experience in Years: {student.experience}")
print(f"Skills: {', '.join(student.skills)}")