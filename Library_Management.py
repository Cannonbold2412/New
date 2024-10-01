class Library:
    def __init__(self):
        self.noBooks = 0
        self.books = []

    def addBook(self, book):
        self.books.append(book)
        self.noBooks = len(self.books)

    def showInfo(self):
        print(f"The Library has {self.noBooks} books. The books are:\n")
        for book in self.books:
            print(book)

l1 = Library()
l1.addBook("48 Laws of Power")
l1.addBook("Power of Money")
l1.addBook("Rich Dad and Poor Dad")
l1.showInfo()
