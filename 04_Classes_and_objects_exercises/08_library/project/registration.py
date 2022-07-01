# In the registration.py, create a class called Registration. Upon initialization, It will not receive anything, but
# we'll have these three methods.
# -	add_user(user: User, library: Library):
# o	Adds the user if we do not have them in the library's user records already
# o	Otherwise, returns the message "User with id = {user_id} already registered in the library!"
# -	remove_user(user: User, library: Library):
# o	Removes the user from the library records if present
# o	Otherwise, returns the message "We could not find such user to remove!"
# -	change_username(user_id: int, new_username: str, library: Library):
# o	If there is a record with the same user id in the library and the username is different than the provided one,
# changes the username with the new one provided and returns the message "Username successfully changed to:
# {new_username} for user id: {user_id}". Changes his username in the rented_books dictionary as well (if present).
# o	If the new username is the same for this id, returns the following message "Please check again the provided username
# - it should be different than the username used so far!".
# o	If there is no record for the provided id returns "There is no user with id = {user_id}!"
from .library import Library

class Registration:

    def add_user(self, user, library):
        if user in library.user_records:
            return f"User with id = {user.user_id} already registered in the library!"
        library.user_records.append(user)

    def remove_user(self, user, library):
        if user not in library.user_records:
            return f"We could not find such user to remove!"
        library.user_records.remove(user)

    def change_username(self, user_id: int, new_username: str, library: Library):
        for user in library.user_records:
            if user.user_id == user_id:
                if user.username == new_username:
                    return f"Please check again the provided username - it should be different than the username used" \
                           f" so far!"
                if user.username in library.rented_books:
                    rented_books = library.rented_books[user.username]
                    library.rented_books.pop(user.username)
                    library.rented_books[new_username] = rented_books
                user.username = new_username
                return f"Username successfully changed to: {new_username} for user id: {user_id}"
        return f"There is no user with id = {user_id}!"


