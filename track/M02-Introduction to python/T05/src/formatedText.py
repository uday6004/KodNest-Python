class StudentProfile:
    def __init__(
        self,
        student_id,
        name,
        course,
        experience
    ):
        # Store all values as instance variables
        self.student_id = student_id
        self.name = name
        self.course = course
        self.experience = experience

    # Create the from_text() alternative constructor
    @classmethod
    def from_text(cls, data):
        parts = data.split("|")
        return cls(int(parts[0]), parts[1], parts[2], int(parts[3]))

data = input().strip()

# Create the StudentProfile object using from_text()
profile = StudentProfile.from_text(data)

# Print the stored profile
print(f"Student ID: {profile.student_id}")
print(f"Name: {profile.name}")
print(f"Course: {profile.course}")
print(f"Experience: {profile.experience} years")