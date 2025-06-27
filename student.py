class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def display(self):
        print(f"Student Name: {self.name}")
        print(f"Marks: {self.marks}")

# Test the class
student1 = Student("Alice", 85)
student1.display()

student2 = Student("Sana", 99)
student2.display()