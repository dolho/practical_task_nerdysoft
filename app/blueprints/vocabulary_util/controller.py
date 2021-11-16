from app.blueprints.vocabulary_util.database_handler.db import SessionLocal
from app.blueprints.vocabulary_util.database_handler.db_handler import VocabularyDatabaseHandler
import collections
import json


class VocabularyController():

    def __init__(self):
        self.__db_handler = VocabularyDatabaseHandler(SessionLocal())

    def add_word(self, word: str):
        try:
            result = self.__db_handler.add_word(word)
        except ValueError:
            return {"http_code": 400, "description": "Word is already in the vocabulary"}
        return {"http_code": 200, "description": "Ok"}

    def add_words(self, words):
        self.__db_handler.add_words(words)

    def replace_words(self, words):
        self.__db_handler.replace_words(words)

    def count_filtered_words(self, filter_string: str):
        letters = collections.Counter(filter_string)
        word_count = self.__db_handler.count_filtered_words(letters)
        return {"http_code": 200, "description": str(word_count)}

    def get_filtered_words(self, filter_string, page=1):
        if page < 1:
            page = 1

        offset, limit = self.__paginator(page)
        letters = collections.Counter(filter_string)
        words = self.__db_handler.get_filtered_words(letters, offset, limit)
        return {"http_code": 200, "description": json.dumps(words)}

    def __paginator(self, page):
        limit = page * 10
        offset = (page - 1) * 10
        return offset, limit