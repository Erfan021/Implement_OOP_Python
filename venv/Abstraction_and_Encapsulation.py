class Library:

    def __init__(self, listOfBooks):
        self.availableBooks = listOfBooks

    def displayBooks(self):
        print() # Encapsulation being done
        print("Books in Library:")
        for books in self.availableBooks:
            print(books)

    def lendBook(self, requestedBook):
        if requestedBook in self.availableBooks: # Encapsulation being done
            self.availableBooks.remove(requestedBook)
            print("Book borrowed")
        else:
            print("Sorry, requested book is not available.")

    def addBook(self, returnedBook):
        self.availableBooks.append(returnedBook) # Encapsulation being done
        print("Book returned to the library.")


class Customer:
    def requestBook(self): # Encapsulation being done
        print("Enter the name of book to borrow: ")
        self.book = input()
        return self.book

    def returnBook(self): # Encapsulation being done
        print("Enter name of book to return: ")
        self.book = input()
        return self.book



customer = Customer()
library = Library(['Life of Pie', 'Matilda', 'Boy', 'Narnia'])

while True:
    print('Enter 1 to display books available in library: ')
    print('Enter 2 to borrow the book: ')
    print('Enter 3 to return the book: ')
    print('Enter 4 to quit: ')
    userInput = int(input())
    if userInput is 1:
        library.displayBooks() # Layer of abstraction performed
    elif userInput is 2:
        requestedBook = customer.requestBook() # Layer of abstraction performed
        library.lendBook(requestedBook)
    elif userInput is 3:
        returnedBook = customer.returnBook() # Layer of abstraction performed
        library.addBook(returnedBook)
    elif userInput is 4:
        quit()
    else:
        print("Enter right option!")


