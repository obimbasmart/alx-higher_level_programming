#!/usr/bin/python3

"""class definition for City class"""


from model_state import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey


class City(Base):
    """ class definition of a City"""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
