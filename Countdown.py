class Countdown:
    def __init__(self, start):
        self.start = start
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value

# Example 1: Iterating over Countdown in a for-loop
print("Example 1:")
countdown1 = Countdown(5)
for num in countdown1:
    print(num)

# Example 2: Iterating over a different Countdown and collecting values
print("\nExample 2:")
countdown2 = Countdown(3)
numbers = [num for num in countdown2]
print(f"Collected numbers: {numbers}")