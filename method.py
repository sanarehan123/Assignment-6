class A:
    def show(self):
        return "Method from class A"

class B(A):
    def show(self):
        return "Method from class B"

class C(A):
    def show(self):
        return "Method from class C"

class D(B, C):
    pass

# Example 1: Creating a D object and calling show()
print("Example 1:")
d1 = D()
print(d1.show())  # Should call B's show() due to MRO
print("MRO for class D:", [cls.__name__ for cls in D.__mro__])

# Example 2: Creating another D object and verifying MRO
print("\nExample 2:")
d2 = D()
print(d2.show())  # Should again call B's show()
print("MRO for class D:", [cls.__name__ for cls in D.mro()])