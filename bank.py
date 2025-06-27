class Bank:
    bank_name = "Default Bank"  # Class variable

    def __init__(self, account_holder):
        self.account_holder = account_holder

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name  # Update class variable

    def display_details(self):
        print(f"Account Holder: {self.account_holder}, Bank: {self.bank_name}")

# Example 1: Create instances and display initial bank name
print("Example 1: Before changing bank name")
account1 = Bank("Alice")
account2 = Bank("Bob")
account1.display_details()
account2.display_details()

# Example 2: Change bank name and show it affects all instances
print("\nExample 2: After changing bank name")
Bank.change_bank_name("Global Bank")
account1.display_details()
account2.display_details()

# Example 3: Create a new instance after changing bank name
print("\nExample 3: New instance after bank name change")
account3 = Bank("Charlie")
account3.display_details()