"""
Assignment 3 — Library Book Catalogue
=======================================
Week 2 · Dlytica Data and AI Foundations Track
Topics: Classes & Objects, Instance Methods, Class Attributes, @classmethod
"""

class Book:
    total_books = 0                         

    def __init__(self, title, author, genre, available=True):
        self.title     = title
        self.author    = author
        self.genre     = genre
        self.available = available
        Book.total_books += 1                


    @classmethod
    def from_dict(cls, data):
        """Create a Book instance from a dictionary."""
        return cls(data["title"], data["author"], data["genre"])

    @classmethod
    def get_total(cls):
        """Return total books registered as a formatted string."""
        return f"Total books registered: {cls.total_books}"


    def borrow(self):
        """Mark book as borrowed. Raise ValueError if already borrowed."""
        if not self.available:
            raise ValueError(f"'{self.title}' is already borrowed.")
        self.available = False

    def return_book(self):
        """Mark book as available. Raise ValueError if not currently borrowed."""
        if self.available:
            raise ValueError(f"'{self.title}' is not currently borrowed.")
        self.available = True


    def __str__(self):
        status = "✓" if self.available else "✗"       
        return f"[{status}] {self.title} | {self.author} | {self.genre}"


print("=" * 55)
print("          LIBRARY BOOK CATALOGUE")
print("=" * 55)

b1 = Book("Python Crash Course", "Eric Matthes", "Programming")
b2 = Book("Sapiens", "Yuval Noah Harari", "History")
b3 = Book.from_dict({
    "title": "Deep Work", "author": "Cal Newport", "genre": "Productivity"
})
b4 = Book("Atomic Habits", "James Clear", "Self-Help")

b1.borrow()
b2.borrow()

print("\n-- Current Catalogue --")
for book in [b1, b2, b3, b4]:
    print(f"  {book}")

print("\n-- Returning 'Python Crash Course' --")
b1.return_book()
print(f"  {b1}")

print(f"\n  {Book.get_total()}")

print("\n-- Testing ValueError (borrow already borrowed book) --")
try:
    b2.borrow()
except ValueError as e:
    print(f"Error caught: {e}")

print("\n-- Testing ValueError (return a non-borrowed book) --")
try:
    b3.return_book()
except ValueError as e:
    print(f"Error caught: {e}")

print("=" * 55)