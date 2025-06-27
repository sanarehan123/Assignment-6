class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

# Example 1: Using the static method directly
print("Example 1:")
result1 = MathUtils.add(5, 3)
print(f"Sum of 5 and 3: {result1}")

# Example 2: Using the static method with different numbers
print("\nExample 2:")
result2 = MathUtils.add(10.5, 4.5)
print(f"Sum of 10.5 and 4.5: {result2}")