#  Library Book
class LibraryBook:
    def __init__(self, title, total_copies, borrowed_copies=0):
        self._title = title
        self.total_copies = total_copies
        self.borrowed_copies = borrowed_copies
    @property
    def title(self):
        return self._title
    @property
    def total_copies(self):
        return self._total_copies
    @total_copies.setter
    def total_copies(self, value):
        if value < 1:
            raise ValueError("Total copies must be at least 1")
        self._total_copies = value
    @property
    def borrowed_copies(self):
        return self._borrowed_copies
    @borrowed_copies.setter
    def borrowed_copies(self, value):
        if value < 0:
            raise ValueError("Borrowed copies cannot be negative")
        if value > self.total_copies:
            raise ValueError("Borrowed copies cannot exceed total copies")
        self._borrowed_copies = value
    @property
    def available_copies(self):
        return self.total_copies - self.borrowed_copies
    def borrow(self, amount):
        if amount <= 0:
            raise ValueError("Borrow amount must be positive")
        if amount > self.available_copies:
            raise ValueError("Not enough available copies")
        self.borrowed_copies += amount
    def return_book(self, amount):
        if amount <= 0:
            raise ValueError("Return amount must be positive")
        if amount > self.borrowed_copies:
            raise ValueError("Cannot return more than borrowed")
        self.borrowed_copies -= amount
# Input

b = LibraryBook("Python Basics", 5)
print(b.title, b.available_copies)

b.borrow(3)
print(b.borrowed_copies, b.available_copies)

b.return_book(1)
print(b.borrowed_copies)

try:
    b.borrow(4)
except ValueError as e:
    print(e)

try:
    b.title = "X"
except AttributeError:
    print("Cannot change title")


# Expected Output
# Python Basics 5
# 3 2
# 2
# Not enough available copies
# Cannot change title