class TrainingBatch:
    batch_name = "Python Batch 1"

    def __init__(self, student_name):
        self.student_name = student_name

    @classmethod
    def update_batch_name(cls, new_batch_name):
        cls.batch_name = new_batch_name


student1_name = input("Enter the Student Name: ").strip()
student2_name = input("Enter the Student Name: ").strip()
new_batch_name = input("Enter the New batch Name: ").strip()

# Create two TrainingBatch objects
obj1 = TrainingBatch(student1_name)
obj2 = TrainingBatch(student2_name)

# Update the shared batch name using the class method
TrainingBatch.update_batch_name(new_batch_name)

# Print the updated value through the class and both objects (Fixed typo)
print(f"Updated Batch: {TrainingBatch.batch_name}")
print(f"{obj1.student_name}: {obj1.batch_name}")
print(f"{obj2.student_name}: {obj2.batch_name}")