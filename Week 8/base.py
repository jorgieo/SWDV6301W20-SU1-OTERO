from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


engine = create_engine("sqlite:///posDB.db", echo=False)

Session = sessionmaker(bind=engine)

Base = declarative_base()