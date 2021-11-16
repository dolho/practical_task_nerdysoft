from app.blueprints.vocabulary_util.database_handler.db import SessionLocal
from app.blueprints.vocabulary_util.database_handler.tables.word import Word
from sqlalchemy.exc import IntegrityError, PendingRollbackError
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.dialects import postgresql
from sqlalchemy.sql.expression import func


class VocabularyDatabaseHandler():

    def __init__(self, session):
        self.__session = session

    def add_word(self, word):
        try:
            self.__session.add(Word(word=word))
            self.__session.commit()
        except (IntegrityError, PendingRollbackError) as e:
            print(e)
            raise ValueError

    def add_words(self, words: list):
        sqlalchemy_words = []
        for i in words:
            sqlalchemy_words.append({"word": i})
        stmt = insert(Word)\
               .on_conflict_do_nothing()
        self.__session.execute(stmt, sqlalchemy_words)
        self.__session.commit()

    def replace_words(self, words: list):
        self.__session.query(Word).delete()
        self.__session.commit()
        self.add_words(words)

    def count_filtered_words(self, letters: dict) -> int:
        """
        The function expects letters to have following structure:
        {'letter': 'quantity'} e.g. {'a': 3, 'b': 2}
        """
        query = self.__session.query(Word)
        for key in letters:
            query = self.__filter_by_count_of_character_amount(query, key, letters[key])
        overall_count = query.count()
        return overall_count

    def get_filtered_words(self, letters: dict, offset, limit) -> list:
        """
                The function expects letters to have following structure:
                {'letter': 'quantity'} e.g. {'a': 3, 'b': 2}
        """
        query = self.__session.query(Word)
        for key in letters:
            query = self.__filter_by_count_of_character_amount(query, key, letters[key])
        all_found_words = query.offset(offset).limit(limit).all()
        result = []
        for i in all_found_words:
            result.append(str(i) + " ")
        return result

    def __filter_by_count_of_character_amount(self, query, letter, quantity_of_letter):
        condition = (func.length(Word.word) - func.length(func.replace(Word.word, letter, '')))
        return query.filter(condition >= quantity_of_letter)