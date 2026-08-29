class Course:
    # Add the constructor and display_course()
    def __init__(self, course_name):
        self.course_name = course_name

    def display_course(self):
        print(f"Course: {self.course_name}")

class CodingCourse(Course):
    pass

course_name = input().strip()
course = CodingCourse(course_name)
course.display_course()
