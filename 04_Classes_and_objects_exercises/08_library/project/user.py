# In the user.py file, create class User. Upon initialization, it should receive user_id (int) and username (string).
# The class should also have an instance attribute books that is an empty list. You should also create 2 instance
# methods:
# -	info() - returns a string containing the books currently rented by the user in ascending order separated by comma
# and space.
# -	__str__() - override the method to get a string in the following format "{user_id}, {username}, {list of rented
# books}"

class User:

    RETURN_SORTED_BOOKS_IN__STR__ = False

    def __init__(self, user_id: int, username: str):
        self.user_id = user_id
        self.username = username
        self.books = []

    def info(self):
        if self.books:
            result = sorted(self.books)
            return ', '.join(result)

    def __str__(self):
        return f"{self.user_id}, {self.username}, " \
            f"{sorted(self.books) if User.RETURN_SORTED_BOOKS_IN__STR__ else self.books}"
