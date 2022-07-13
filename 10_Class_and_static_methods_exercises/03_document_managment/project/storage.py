# Upon initialization the class Storage will not receive any parameters. It should have 3 instance attributes:
# categories (empty list), topics (empty list), documents (empty list). The class should have the following methods:
# •	add_category(category:Category) - add the category if it is not in the list
# •	add_topic(topic:Topic) - add the topic if it does not exist
# •	add_document(document:Document) - add the document if it does not exist
# •	edit_category(category_id: int, new_name:str) - edit the name of the category with the provided id
# •	edit_topic(topic_id: int, new_topic: str, new_storage_folder: str) - edit the topic with the given id
# •	edit_document(document_id: int, new_file_name: str) - edit the document with the given id
# •	delete_category(category_id) - delete the category with the provided id
# •	delete_topic(topic_id) - delete the topic with the provided id
# •	delete_document(document_id) - delete the document with the provided id
# •	get_document(document_id) - return the document with the provided id
# •	__repr__() - returns a string representation of each document on separate lines
from .category import Category
from .topic import Topic
from .document import Document

class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category: Category):
        storage_category = self.__find_category_by_id(category.id)

        if storage_category is None:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        storage_topic = self.__find_topic_by_id(topic.id)

        if storage_topic is None:
            self.topics.append(topic)

    def add_document(self, document: Document):
        storage_document = self.get_document(document.id)

        if storage_document is None:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        category = self.__find_category_by_id(category_id)
        category.edit(new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        topic = self.__find_topic_by_id(topic_id)
        topic.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str):
        document = self.get_document(document_id)
        document.edit(new_file_name)

    def delete_category(self, category_id: int):
        category = self.__find_category_by_id(category_id)
        self.categories.remove(category)

    def delete_topic(self, topic_id: int):
        topic = self.__find_topic_by_id(topic_id)
        self.topics.remove(topic)

    def delete_document(self, document_id: int):
        document = self.get_document(document_id)
        self.documents.remove(document)

    def get_document(self, document_id):
        for document in self.documents:
            if document.id == document_id:
                return document

    def __repr__(self):
        return '\n'.join([repr(x) for x in self.documents])

    def __find_category_by_id(self, category_id):
        for category in self.categories:
            if category.id == category_id:
                return category

    def __find_topic_by_id(self, topic_id):
        for topic in self.topics:
            if topic.id == topic_id:
                return topic


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        