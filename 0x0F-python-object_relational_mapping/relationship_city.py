#!/usr/bin/python3

'''
contains the class definition of a City and class instance
attributes id and name that represent columns of auto generated
unique integer and a string of 128 characters repectively. Now
known as the relationship_city
'''
from relationship_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


class City(Base):
    '''Defines class City that inherits from class Base'''
    __tablename__ = "cities"
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
