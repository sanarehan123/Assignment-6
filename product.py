class Product:
    def __init__(self, name, price):
        self.name = name
        self._price = price  # Private attribute

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value

    @price.deleter
    def price(self):
        del self._price

# Example 1: Using getter and setter
print("Example 1:")
product1 = Product("Laptop", 1000)
print(f"Product: {product1.name}, Price: {product1.price}")  # Get price
product1.price = 1200  # Set new price
print(f"Updated Price: {product1.price}")
try:
    product1.price = -50  # Should raise ValueError
except ValueError as e:
    print(f"Error: {e}")

# Example 2: Using getter, setter, and deleter
print("\nExample 2:")
product2 = Product("Phone", 500)
print(f"Product: {product2.name}, Price: {product2.price}")  # Get price
product2.price = 600  # Set new price
print(f"Updated Price: {product2.price}")
del product2.price  # Delete price
try:
    print(product2.price)  # Should raise AttributeError
except AttributeError as e:
    print(f"Error: {e}")