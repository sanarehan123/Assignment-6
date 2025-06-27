class Book:
    total_books = 0  # Class variable to track total books

    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.increment_book_count()  # Call class method to increment count

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1  # Increment the class variable

    @classmethod
    def get_total_books(cls):
        return cls.total_books

    def display(self):
        print(f"Title: {self.title}, Author: {self.author}")

# Example 1: Creating books and checking total count
print("Example 1:")
book1 = Book("1984", "George Orwell")
book1.display()
print(f"Total books: {Book.get_total_books()}")

# Example 2: Creating more books and checking updated count
print("\nExample 2:")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
book3 = Book("Pride and Prejudice", "Jane Austen")
book2.display()
book3.display()
print(f"Total books: {Book.get_total_books()}")