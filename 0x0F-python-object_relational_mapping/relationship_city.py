#!/usr/bin/python3
""" City Class def """
from sqlalchemy import Column, Integer, String
from relationship_state import Base
from sqlalchemy import ForeignKey


class City(Base):
    """
    City class sup calss from Base
    ORM first try :D

    Attributes:
        id: id that will be asigned from the sql
        name: name of the state
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
