# The Document class should receive the following parameters upon initialization: id: int, category_id: int,
# topic_id: int, file_name: str. The class should also have one more attribute called tags (empty list). The class
# should also have 4 methods:
# •	from_instances(id: int, category: Category, topic: Topic, file_name: str) - create a new instance using the provided
# category and topic instances
# •	add_tag(tag_content: str) - if the tag is not already in the tags list, add it to the tags list
# •	remove_tag(tag_content:str) - if the tag is in the tags list, delete it
# •	edit(file_name: str) - change the file name with the given one
# •	__repr__() - returns a string representation of a document in the format: "Document {id}: {file_name}; category
# {category_id}, topic {topic_id}, tags: {tags joined by comma and space)}"
from .category import Category
from .topic import Topic


class Document:
    def __init__(self, id: int, category_id: int, topic_id: int, file_name: str):

        self.id = id
        self.category_id = category_id
        self.topic_id = topic_id
        self.file_name = file_name
        self.tags = []

    @classmethod
    def from_instances(cls, id: int, category: Category, topic: Topic, file_name: str):
        return cls(id, category.id, topic.id, file_name)

    def add_tag(self, tag_content: str):
        if tag_content in self.tags:
            return
        self.tags.append(tag_content)


    def remove_tag(self, tag_content):
        if tag_content not in self.tags:
            return
        self.tags.remove(tag_content)

    def edit(self, file_name: str):
        self.file_name = file_name

    def __repr__(self):
        return f"Document {self.id}: {self.file_name}; category {self.category_id}, topic {self.topic_id}, " \
               f"tags: {', '.join(tag for tag in self.tags)}"