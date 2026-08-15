class JobDescription:
    def __init__(self, job_id, company, role, location, required_skills, is_active):
        self.job_id = job_id
        self.company = company
        self.role = role
        self.location = location
        self.required_skills = required_skills
        self.is_active = is_active

    def __str__(self):
        skills_str = ", ".join(self.required_skills)
        status_str = "Active" if self.is_active else "Closed"
        return (
            f"JOB DESCRIPTION\n"
            f"Job ID: {self.job_id}\n"
            f"Company: {self.company}\n"
            f"Role: {self.role}\n"
            f"Location: {self.location}\n"
            f"Required Skills: {skills_str}\n"
            f"Status: {status_str}"
        )

# Read inputs
job_id = int(input("Enter the Job ID:").strip())
company = input("Enter the Company name:").strip()
role = input("Enter the Role:").strip()
location = input("Enter the Location:").strip()
skills_input = input("Enter the skills:").strip()
status_input = input("Enter the status:").strip()

# Process required_skills list (splitting by comma)
required_skills = [skill.strip() for skill in skills_input.split(',')]

# Convert status input ("Yes"/"No") to boolean
is_active = status_input.lower() == 'yes'

# Create instance and print formatted description
job = JobDescription(job_id, company, role, location, required_skills, is_active)
print(job)