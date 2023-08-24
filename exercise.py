class library:
    def __init__(self):
        self.nobooks = 0
        self.book = []

    def addbook(self,book):
        self.book.append(book)
        self.nobooks = len(self.book)
    
    def showinfo(self):
        print(f"The library has {self.nobooks} books")
        for book in self.book:
            print(book)
l1 = library()
l1.addbook("harry potter")
l1.addbook("harry potter 2")
l1.addbook("harry potter 3")
l1.showinfo()
