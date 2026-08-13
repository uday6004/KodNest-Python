class StudentProfile:
    # 1. Constructor: Sets up the data for a specific student
    def __init__(self, student_id, name, course, score, is_placed):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.score = score
        self.is_placed = is_placed

    # 2. String representation: Defines how to print the card
    def __str__(self):
        status = "Placed" if self.is_placed else "Not Placed"
        return (
            f"STUDENT PROFILE\n"
            f"Student ID: {self.student_id}\n"
            f"Name: {self.name}\n"
            f"Course: {self.course}\n"
            f"Score: {self.score:.1f}\n"
            f"Placement Status: {status}"
        )

student = StudentProfile(student_id = 55,name = "Uday",course = "BE",score = 80.88,is_placed = True)
print(student)