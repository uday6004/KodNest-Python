class StudentProfile:
    def __init__(self, student_id, name, course, score=0.0, skill=None, is_placed=False):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.score = score
        self.skill = [] if skill is None else list(skill)
        self.is_placed = is_placed
    def __str__(self):
        skill_text = (",".join(self.skill)) if self.skill else "No Skills"
        placement_status = "Placed" if self.is_placed else "Not Placed"
        return (
            f"Student ID: {self.student_id}\n"
            f"Name: {self.name}\n"
            f"Course: {self.course}\n"
            f"Score: {self.score:.2f}\n"
            f"Skills: {skill_text}\n"
            f"Placement Status: {placement_status}"
        )
# pyrefly: ignore [parse-error]
student = StudentProfile(student_id = 55,name = "Uday",course = "BE",score = 80.88,skill = ["python"],is_placed = True)
print(student)