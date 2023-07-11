from project.category import Category
from project.topic import Topic
from project.document import Document


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        category = self._find_category_by_id(category_id)
        if category:
            category.edit(new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        topic = self._find_topic_by_id(topic_id)
        if topic:
            topic.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str):
        document = self._find_document_by_id(document_id)
        if document:
            document.edit(new_file_name)

    def delete_category(self, category_id: int):
        category = self._find_category_by_id(category_id)
        if category:
            self.categories.remove(category)

    def delete_topic(self, topic_id: int):
        topic = self._find_topic_by_id(topic_id)
        if topic:
            self.topics.remove(topic)

    def delete_document(self, document_id: int):
        document = self._find_document_by_id(document_id)
        if document:
            self.documents.remove(document)

    def get_document(self, document_id: int):
        return self._find_document_by_id(document_id)

    def __repr__(self):
        return '\n'.join([repr(document) for document in self.documents])

    def _find_category_by_id(self, category_id: int):
        for category in self.categories:
            if category.id == category_id:
                return category
        return None

    def _find_topic_by_id(self, topic_id: int):
        for topic in self.topics:
            if topic.id == topic_id:
                return topic
        return None

    def _find_document_by_id(self, document_id: int):
        for document in self.documents:
            if document.id == document_id:
                return document
        return None
