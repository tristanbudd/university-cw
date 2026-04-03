# Challenge #2 - Completing Library Code
class Book:

    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True

    def borrow_book(self):
        self.available = False

    def return_book(self):
        self.available = True

    def __str__(self):
        return f"{self.title} by {self.author} ({self.isbn})"


class DigitalBook(Book):

    def __init__(self, title, author, isbn):
        super().__init__(title, author, isbn)
        self.compatibility = {'Kindle'}

    def borrow_book(self):
        pass

    def return_book(self):
        pass

    def __str__(self):
        return f"{super().__str__()} [Compatibility: {', '.join(self.compatibility)}]"


class Library:

    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title:
                if book.available:
                    book.borrow_book()

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                if not book.available:
                    book.return_book()

    def __str__(self):
        to_return = "Library contains:\n"
        for book in self.books:
            to_return += f"{book}\n"
        return to_return


def test_book():
    book = Book('Frankenstein', 'Mary Shelley', '978-0486282114')
    print(book)

    book.borrow_book()
    book.return_book()


def test_digital_book():
    digital_book = DigitalBook(
        'Orlando: A Biography', 'Virginia Woolf', '978-0156031516')
    print(digital_book)

    digital_book.borrow_book()
    digital_book.return_book()


def test_library():
    Book("The Great Gatsby", "F. Scott Fitzgerald", "978-0743273565")
    Book("1984", "George Orwell", "978-0451524935")
    Book("Jane Eyre", "Charlotte Bronte", "978-0141441146")
    DigitalBook("1984", "George Orwell", "978-0451524935")

    library = Library()
    library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald", "978-0743273565"))
    print(library)
    library.add_book(Book("1984", "George Orwell", "978-0451524935"))
    test_book()
    print(library)
    library.add_book(Book("Jane Eyre", "Charlotte Bronte", "978-0141441146"))
    test_digital_book()
    print(library)
    library.add_book(DigitalBook("1984", "George Orwell", "978-0451524935"))
    test_book()
    print(library)


if __name__ == "__main__":
    test_library()

test_library()