class Counter:
    count = 0  # Class variable to track number of objects

    def __init__(self):
        Counter.count += 1  # Increment count when a new object is created

    @classmethod
    def display_count(cls):
        print(f"Total objects created: {cls.count}")

# Example 1: Creating a few objects and displaying the count
print("Example 1:")
obj1 = Counter()
obj2 = Counter()
obj3 = Counter()
Counter.display_count()

# Example 2: Creating additional objects and displaying the count
print("\nExample 2:")
obj4 = Counter()
obj5 = Counter()
Counter.display_count()