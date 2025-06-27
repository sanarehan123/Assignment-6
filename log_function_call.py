def log_function_call(func):
    def wrapper():
        print("Function is being called")
        return func()
    return wrapper

@log_function_call
def say_hello():
    print("Hello, World!")

# Example 1: Calling the decorated function once
print("Example 1:")
say_hello()

# Example 2: Calling the decorated function multiple times
print("\nExample 2:")
say_hello()
say_hello()