class Employee:

    def show_details(self):
        pass


class PermanentEmployee(Employee):

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_details(self):
        print(f"{self.name} - Permanent - Salary: {self.salary}")


class ContractEmployee(Employee):

    def __init__(self, name, contract_months):
        self.name = name
        self.contract_months = contract_months

    def show_details(self):
        print(f"{self.name} - Contract - Duration: {self.contract_months} months")


permanent_name = input()
salary = int(input())
contract_name = input()
contract_months = int(input())

# Create both objects
perm_emp = PermanentEmployee(permanent_name, salary)
contract_emp = ContractEmployee(contract_name, contract_months)

# Store both objects in one list
employees = [perm_emp, contract_emp]

# Process the list using one loop
for emp in employees:
    emp.show_details()