from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Example 1: Creating a Rectangle object and calculating area
print("Example 1:")
rect1 = Rectangle(5, 3)
print(f"Rectangle area (width=5, height=3): {rect1.area()}")

# Example 2: Creating another Rectangle and attempting to instantiate Shape
print("\nExample 2:")
rect2 = Rectangle(4, 6)
print(f"Rectangle area (width=4, height=6): {rect2.area()}")
try:
    shape = Shape()  # Should raise TypeError
except TypeError as e:
    print(f"Error creating Shape instance: {e}")