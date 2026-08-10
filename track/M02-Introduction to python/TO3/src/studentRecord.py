name = input()
course = input()
score = int(input("enter the score:"))

# Store in a tuple
student_record = (name, course, score)

# Unpack the tuple
student_name, student_course, student_score = student_record

# Display the unpacked values
print("Name:", student_name)
print("Course:", student_course)
print("Score:", student_score)