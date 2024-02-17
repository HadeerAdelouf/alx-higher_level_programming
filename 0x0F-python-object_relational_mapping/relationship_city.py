#!/usr/bin/python3
"""
Defines a state model that contain the class definition
 of a City and an instance Base = declarative_base()
"""
from relationship_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """
    City class that inherits from Base

    Attrs:
        id: Id city
        name: Name of the city
        state_id: State id
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
