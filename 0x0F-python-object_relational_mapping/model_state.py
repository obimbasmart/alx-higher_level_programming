#!/usr/bin/python3

'''file that contains the class definition of a State '''

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String
import sys


_, user_name, passwd, db_name = sys.argv
engine = create_engine(
    'mysql+mysqldb://{}:{}@localhost/{}'.format(user_name, passwd, db_name))
session = sessionmaker(bind=engine)

Base = declarative_base()


class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
