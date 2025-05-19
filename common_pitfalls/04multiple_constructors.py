class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @classmethod
    def from_string(cls, book_str):
        title, author = book_str.split("-")
        return cls(title.strip(), author.strip())

# Usage
book1 = Book("Python 101", "John Doe")
book2 = Book.from_string("Python 101 - John Doe")

print(book1.title, book1.author)
print(book2.title, book2.author)
