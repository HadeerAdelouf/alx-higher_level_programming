#!/usr/bin/python3
"""
Python file that contains the class definition of a State and an instance
"""
from sqlalchemy import column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class state(Base):
    """
    state class inhert from Base
    attr:
       id : id state
       name: Name of state
    """
    __tablename__ = "states"
    id = column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = column(String(128), nullable=False)
