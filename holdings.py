class Holdings:
    """Manages the library's book holdings."""

    def __init__(self, books):
        self.books = books

    def get_on_shelf(self, title):
        """Return the number of available copies of a book."""

        if title not in self.books:
            return 0

        holding = self.books[title]

        copies = holding["copies"]
        borrowed = holding["borrowed"]

        return copies - borrowed

    
    def borrow(self, title, quantity):
        """Increase the borrowed quantity of a book."""

        available = self.get_on_shelf(title)

        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")

        if available < quantity:
            raise ValueError(f"Not enough copies of '{title}' available.")

        self.books[title]["borrowed"] += quantity
