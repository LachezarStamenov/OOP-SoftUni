# The Task class should also have five additional methods:
# -	change_name(new_name: str)
# o	Changes the name of the task and returns the new name.
# o	If the new name is the same as the current name, returns "Name cannot be the same."
# -	change_due_date(new_date: str)
# o	Changes the due date of the task and returns the new date.
# o	If the new date is the same as the current date, returns "Date cannot be the same."
# -	add_comment(comment: str)
# o	Adds a comment to the task.
# -	edit_comment(comment_number: int, new_comment: str)
# o	The comment number value represents the index of the comment we want to edit. The method should change the
# comment and return all the comments, separated by comma and space (", ")
# o	If the comment number is out of range, returns "Cannot find comment."
# -	details()
# o	Returns the task's details in this format:
# "Name: {task_name} - Due Date: {due_date}"


class Task:
    def __init__(self, name: str, due_date: str):
        self.name = name
        self.due_date = due_date
        self.comments = []
        self.completed = False

    def change_name(self, new_name: str):
        if self.name == new_name:
            return f"Name cannot be the same."
        self.name = new_name
        return self.name

    def change_due_date(self, new_date: str):
        if self.due_date == new_date:
            return f"Date cannot be the same."
        self.due_date = new_date
        return self.due_date

    def add_comment(self, comment: str):
        self.comments.append(comment)

    def edit_comment(self, content_number: int, new_comment: str):
        try:
            self.comments[content_number] = new_comment
            return ", ".join(self.comments)
        except IndexError:
            return 'Cannot find comment.'

    def details(self):
        return f"Name: {self.name} - Due Date: {self.due_date}"
