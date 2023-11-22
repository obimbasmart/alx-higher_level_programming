#!/usr/bin/python3

"""file that contains the class definition of a State,
an instance of Base = declarative_base()"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """ class definition of a State"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", back_populates="state",
                          cascade="all, delete-orphan")
