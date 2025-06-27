def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    setattr(cls, 'greet', greet)  # Add greet method to the class
    return cls

@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f"My name is {self.name}"

# Example 1: Creating a Person object and calling greet
print("Example 1:")
person1 = Person("Alice")
print(person1.introduce())
print(person1.greet())

# Example 2: Creating another Person object and testing both methods
print("\nExample 2:")
person2 = Person("Bob")
print(person2.introduce())
print(person2.greet())