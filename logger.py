class Logger:
    def __init__(self, name):
        self.name = name
        print(f"Logger object '{self.name}' created")

    def __del__(self):
        print(f"Logger object '{self.name}' destroyed")

# Example 1: Creating and destroying a single Logger object
print("Example 1:")
obj1 = Logger("First")
del obj1  # Explicitly delete to trigger destructor

# Example 2: Creating multiple Logger objects in a scope
print("\nExample 2:")
def create_loggers():
    obj2 = Logger("Second")
    obj3 = Logger("Third")
create_loggers()  # Objects destroyed when function scope ends