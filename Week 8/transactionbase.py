from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


engine = create_engine("sqlite:///transactionDB.db", echo=False)
session = sessionmaker(bind=engine)()

Base = declarative_base()