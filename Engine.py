class Engine:
    def __init__(self, type):
        self.type = type

    def start(self):
        return f"The {self.type} engine is starting!"

class Car:
    def __init__(self, model, engine):
        self.model = model
        self.engine = engine  # Composition: Engine object as an attribute

    def start_car(self):
        return f"Car {self.model}: {self.engine.start()}"

# Example 1: Creating a Car with an Engine and starting it
print("Example 1:")
engine1 = Engine("V6")
car1 = Car("Toyota Camry", engine1)
print(car1.start_car())

# Example 2: Creating another Car with a different Engine
print("\nExample 2:")
engine2 = Engine("Electric")
car2 = Car("Tesla Model 3", engine2)
print(car2.start_car())