# Read the course details
course_name = input()
current_week = input()
course_status = input()

# Create the original tuple
course_details = (course_name, current_week, course_status)

# Read the updated week
updated_week = input()

# Create and assign a new tuple
course_details = (course_details[0], updated_week, course_details[2])

# Display the updated tuple
print(course_details)
