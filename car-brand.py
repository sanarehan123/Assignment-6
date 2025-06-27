class Car:
    def __init__(self, brand):
        self.brand = brand  # Public variable

    def start(self):
        print(f"The {self.brand} car is starting!")

# Example 1: Creating a Car object and testing brand and start
print("Example 1:")
car1 = Car("Toyota")
print(f"Car brand: {car1.brand}")
car1.start()

# Example 2: Creating another Car object and testing brand and start
print("\nExample 2:")
car2 = Car("Honda")
print(f"Car brand: {car2.brand}")
car2.start()