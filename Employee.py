class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name          # Public variable
        self._salary = salary     # Protected variable
        self.__ssn = ssn          # Private variable

    def display(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self._salary}")
        print(f"SSN: {self.__ssn}")

# Example 1: Accessing all variables directly
print("Example 1: Accessing variables directly")
emp1 = Employee("Alice", 50000, "123-45-6789")
print(f"Public name: {emp1.name}")          # Should work
print(f"Protected salary: {emp1._salary}")  # Should work (convention-based)
try:
    print(f"Private SSN: {emp1.__ssn}")    # Should raise AttributeError
except AttributeError as e:
    print(f"Error accessing __ssn: {e}")

# Example 2: Accessing private variable using name mangling
print("\nExample 2: Accessing private variable with name mangling")
emp2 = Employee("Bob", 60000, "987-65-4321")
print(f"Public name: {emp2.name}")          # Should work
print(f"Protected salary: {emp2._salary}")  # Should work
print(f"Private SSN (mangled): {emp2._Employee__ssn}")  # Should work using mangled name

# Example 3: Using display method to access all variables
print("\nExample 3: Using display method")
emp3 = Employee("Charlie", 75000, "456-78-9012")
emp3.display()  # Should access all variables safely