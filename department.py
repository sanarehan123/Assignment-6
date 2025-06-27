class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def display(self):
        return f"Employee: {self.name}, ID: {self.id}"

class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []  # List to store references to Employee objects

    def add_employee(self, employee):
        self.employees.append(employee)  # Aggregate Employee object

    def display_employees(self):
        print(f"Department: {self.name}")
        if self.employees:
            for emp in self.employees:
                print(emp.display())
        else:
            print("No employees in this department")

# Example 1: Creating employees and adding them to a department
print("Example 1:")
emp1 = Employee("Alice", 101)
emp2 = Employee("Bob", 102)
dept1 = Department("Engineering")
dept1.add_employee(emp1)
dept1.add_employee(emp2)
dept1.display_employees()

# Example 2: Creating a new department and reusing an existing employee
print("\nExample 2:")
dept2 = Department("Marketing")
dept2.add_employee(emp1)  # Reusing emp1 from Example 1
emp3 = Employee("Charlie", 103)
dept2.add_employee(emp3)
dept2.display_employees()
print(f"\nEmployee still exists independently: {emp1.display()}")