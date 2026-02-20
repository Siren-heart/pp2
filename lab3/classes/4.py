class Employee:
    company_name = "Tech Corp"
    
    def __init__(self, name):
        self.name = name

emp1 = Employee("Sarah")
emp2 = Employee("Mike")

print(f"{emp1.name} works at {emp1.company_name}")
print(f"{emp2.name} works at {emp2.company_name}")

Employee.company_name = "Global Tech"
print(f"After company name change, {emp1.name} now works at {emp1.company_name}")