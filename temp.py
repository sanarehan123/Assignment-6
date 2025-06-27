class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

# Example 1: Converting a single Celsius temperature
print("Example 1:")
celsius1 = 25
fahrenheit1 = TemperatureConverter.celsius_to_fahrenheit(celsius1)
print(f"{celsius1}°C is equal to {fahrenheit1}°F")

# Example 2: Converting multiple Celsius temperatures
print("\nExample 2:")
temps = [0, 37, 100]
for c in temps:
    f = TemperatureConverter.celsius_to_fahrenheit(c)
    print(f"{c}°C is equal to {f}°F")