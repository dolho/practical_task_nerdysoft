from sqlalchemy import Table, Column, Integer, String, MetaData
from app.blueprints.vocabulary_util.database_handler.db import engine
meta = MetaData()

words = Table(
   'words', meta,
   Column('word', String, primary_key = True),
)
print(type(words.columns))
meta.create_all(engine)
