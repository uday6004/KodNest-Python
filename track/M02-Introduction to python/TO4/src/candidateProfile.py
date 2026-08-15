class CandidateProfile:
    def __init__(self, name, email, score):
        self.name = name
        self._email = email
        self.__score = score

    def get_email(self):
        return self._email

    def get_score(self):
        return self.__score

# Read inputs
name = input("Enter the Name: ").strip()
email = input("Enter the Email: ").strip()
score = int(input("Enter the Score: ").strip())

# Create instance
candidate = CandidateProfile(name, email, score)

# Print formatted profile using direct access for public and methods for protected/private
print("CANDIDATE PROFILE")
print(f"Name: {candidate.name}")
print(f"Email: {candidate.get_email()}")
print(f"Score: {candidate.get_score()}")