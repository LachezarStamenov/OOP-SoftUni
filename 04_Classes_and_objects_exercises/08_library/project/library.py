# In the library.py create a class Library. Upon initialization, it will not receive anything, but it should have the
# following instance attributes:
# o	user_records - an empty list that will store the users (users objects) of the library
# o	books_available - an empty dictionary that will keep information regarding the authors (key: str) and the books
# available for each of the authors (list of strings)
# o	rented_books - an empty dictionary that will keep information regarding the usernames (key: str) and nested
# dictionary as a value in which will keep information regarding the book names (key: str) and days left before
# returning the book to the library (int) - ({usernames: {book names: days to return}}).
# You should also create 2 additional instance methods:
# -	get_book(author: str, book_name: str, days_to_return: int, user: User):
# o	If the book is available in the library adds it to the books list for this user, updates the library records
# (rented_books and available_books dicts), and returns the following message: "{book_name} successfully rented
# for the next {days_to_return} days!"
# o	If it is already rented, returns the following message "The book "{book_name}" is already rented and will be
# available in {days_to_return provided by the user rented the book} days!"
# -	return_book(author:str, book_name:str, user: User):
# o	If the book is in the user's books list, returns it in the library (update books_available and rented_books
# class attributes) and removes it from the books list for this user
# o	Otherwise, returns the following message "{username} doesn't have this book in his/her records!"
from .user import User


class Library:

    def __init__(self):
        self.user_records = []
        self.books_available = {}
        self.rented_books = {}

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User):
        if author in self.books_available and book_name in self.books_available[author]:
            user.books.append(book_name)
            self.books_available[author].remove(book_name)

            if user.username not in self.rented_books:
                self.rented_books[user.username] = {}
            self.rented_books[user.username][book_name] = days_to_return
            return f"{book_name} successfully rented for the next {days_to_return} days!"

        for user_books in self.rented_books.values():
            if book_name in user_books:
                return f'The book "{book_name}" is already rented and will be available in {user_books[book_name]} days!'

    def return_book(self, author: str, book_name: str, user: User):
        if book_name not in user.books:
            return f"{user.username} doesn't have this book in his/her records!"
        user.books.remove(book_name)
        self.books_available[author].append(book_name)
        self.rented_books[user.username].pop(book_name)


