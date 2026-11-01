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
