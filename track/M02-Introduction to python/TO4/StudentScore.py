class StudentProfile:
    def __init__(self, name, score):
        self.name = name
        # Store the score in a private attribute
        self.__score = score
        
    def get_score(self):
        # Return the private score
        return self.__score
        
    def set_score(self, new_score):
        # Update and return True when the score is valid
        # Return False without updating when it is invalid
        if 0 <= new_score <= 100:
            self.__score = new_score
            return True
        return False

# Read inputs
name = input("Enter the Name: ").strip()
initial_score = int(input("Enter the Initial Score: "))
new_score = int(input("Enter the New Score: "))

# Create exactly one StudentProfile object
student = StudentProfile(name, initial_score)

# Call the setter and display whether the update was successful
if student.set_score(new_score):
    print("Score Updated")
else:
    print("Invalid Score")

print(f"Name: {student.name}")
# Display the final score using the getter
print(f"Final Score: {student.get_score()}")