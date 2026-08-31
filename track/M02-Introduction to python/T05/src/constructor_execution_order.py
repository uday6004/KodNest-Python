class Employee:
    def __init__(self, name):
        print("Employee constructor")
        self.name = name

class Developer(Employee):
    def __init__(self, name):
        print("Developer constructor started")
        super().__init__(name)
        print("Developer constructor completed")

name = input().strip()
dev = Developer(name)
print(f"Developer: {dev.name}")