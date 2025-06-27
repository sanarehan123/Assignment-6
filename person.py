class Person:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"Name: {self.name}")

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)  # Call base class constructor
        self.subject = subject

    def display(self):
        super().display()  # Call base class display method
        print(f"Subject: {self.subject}")

# Example 1: Creating a Person and a Teacher object
print("Example 1:")
person1 = Person("Alice")
teacher1 = Teacher("Bob", "Mathematics")
person1.display()
teacher1.display()

# Example 2: Creating multiple Teacher objects
print("\nExample 2:")
teacher2 = Teacher("Carol", "English")
teacher3 = Teacher("Dave", "Science")
teacher2.display()
teacher3.display()