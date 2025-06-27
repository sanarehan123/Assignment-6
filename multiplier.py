class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return self.factor * value

# Example 1: Testing with callable() and calling the object
print("Example 1:")
multiplier1 = Multiplier(3)
print(f"Is multiplier1 callable? {callable(multiplier1)}")  # Check if object is callable
result1 = multiplier1(5)  # Call object like a function
print(f"Multiplying 5 by factor 3: {result1}")

# Example 2: Using a different factor and multiple calls
print("\nExample 2:")
multiplier2 = Multiplier(2.5)
print(f"Is multiplier2 callable? {callable(multiplier2)}")  # Check if object is callable
result2 = multiplier2(10)  # Call with one value
result3 = multiplier2(4)   # Call with another value
print(f"Multiplying 10 by factor 2.5: {result2}")
print(f"Multiplying 4 by factor 2.5: {result3}")