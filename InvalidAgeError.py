class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be 18 or older")
    return f"Age {age} is valid"

# Example 1: Handling a valid age
print("Example 1:")
try:
    result = check_age(25)
    print(result)
except InvalidAgeError as e:
    print(f"Error: {e}")

# Example 2: Handling an invalid age
print("\nExample 2:")
try:
    result = check_age(15)
    print(result)
except InvalidAgeError as e:
    print(f"Error: {e}")

# Example 3: Testing multiple ages
print("\nExample 3:")
ages = [20, 17, 30]
for age in ages:
    try:
        result = check_age(age)
        print(result)
    except InvalidAgeError as e:
        print(f"Error for age {age}: {e}")