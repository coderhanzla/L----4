class Libarary:
    def __init__(self ,books):
        self.books = books
        print("Welcome to Libarary")

    def display_books(self):
        print("\n Book is available in Libarary")
        for book in self.books:
            print(book)
            print()

    def lend_books(self ,book):
        if book in self.books:
            self.books.remove(book)
            print(f"You have borrowed {book} enjoy reading it .. . ..")
        else:
             print(f"Book is not available")

    def return_book (self ,book):
        self.books.append(book)
        print(f"Thank you for returning the book")

    def add_book(self ,book):
       self.books.append(book)
       print(f"The book {book} is added to the libarary")

    def __del__(self):
        print("\n Thanks for visiting out the libarary")


l=Libarary(["Harry potter" , "Encyclopedia" , "Quran" , "Bible" , "Gita"])

l.display_books()
l.lend_books("Quran")
l.return_book("Quran")
l.add_book("Humming Bird")


    

        