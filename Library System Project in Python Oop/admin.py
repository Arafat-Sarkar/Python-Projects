from book import *
from User import *

class Admin:
    def __init__(self):
        self.books = []
        self.users = {}

    def add_book(self, book_id , book_name, book_quantity):
        for book in self.books:
            if book.id == book_id:
                print("Book Already Exist")
        new_book = Book(book_id,book_name,book_quantity)
        self.books.append(new_book)
        print("Book Added Successfully")

    def print_all_book(self):
        books_list =  []

        for book in self.books:
            books_list.append(book.name)
        if not books_list:
            print("There are no books")
        
        return ", ".join(books_list)
    
    def search_for_book(self, query):
        found_books = [book.name for book in self.books if book.name[:len(query)].upper() == query.upper()]
        if not found_books:
            return f"No book found"
        return found_books
    
    def add_user(self, user_id, user_name):
        for user in self.users:
            if user.id == user_id:
                print("User Already Exist")
        new_user = User( user_id, user_name)
        self.users[new_user] = None
        print("User created successfully !")


