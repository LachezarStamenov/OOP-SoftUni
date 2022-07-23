from .user import User


class MovieApp:
    def __init__(self):
        self.movies_collection = []
        self.users_collection = []

    def check_if_user_exists(self, username):
        for user in self.users_collection:
            if user.username == username:
                return True
        return False


    def register_user(self, username, age):
        if self.check_if_user_exists(username):
            raise Exception('User already exists!')
        new_user = User(username, age)
        self.users_collection.append(new_user)
        return f'{username} registered successfully.'

