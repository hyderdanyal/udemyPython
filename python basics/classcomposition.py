from typing import List

class BookShelf:
    def __init__(self, *books: List): #type hinting
        self.books = books

    def __str__(self):
        return f"Bookshelf with {len(self.books)} books."

shelf = BookShelf(300)
print(shelf)

class Book(BookShelf):
    def __init__(self, name: str): #type hinting
        self.name = name


    def __str__(self) -> str: #type hinting
        return f"Book {self.name}"

book = Book("Harry Potter")
book2 = Book("Python")
print(book)
shelf = BookShelf(book, book2)

print(shelf)