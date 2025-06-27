class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
    def bark(self):
        print(f"{self.name} says: Woof! Woof!")

# Example 1: Creating a Dog object and calling bark
print("Example 1:")
dog1 = Dog("Max", "Golden Retriever")
print(f"Dog: {dog1.name}, Breed: {dog1.breed}")
dog1.bark()

# Example 2: Creating another Dog object and calling bark
print("\nExample 2:")
dog2 = Dog("Bella", "Labrador")
print(f"Dog: {dog2.name}, Breed: {dog2.breed}")
dog2.bark()