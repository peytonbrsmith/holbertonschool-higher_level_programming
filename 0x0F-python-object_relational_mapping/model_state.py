#!/usr/bin/python3
"""
State class definition
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """[State class definition]

    Arguments:
        id {[int]} -- [id for state]
        name {[string]} -- [name for state]
    """
    __tablename__ = 'states'
    id = Column('id', Integer, primary_key=True,
                nullable=False, autoincrement=True)
    name = Column('name', String(128), nullable=False)
