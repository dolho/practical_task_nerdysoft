from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()

class Word(Base):
     __tablename__ = 'words'
     word = Column(String, primary_key=True)


     def __repr__(self):
        return f'<Word>: {self.word}'

     def __str__(self):
         return self.word