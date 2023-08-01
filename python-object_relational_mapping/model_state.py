#!/usr/bin/python3
"""Base class"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class State(Base):
    """class base"""
    __tablename__ = 'states'
    id = Column(Integer,
                unique=True,
                primary_key=True,
                autoincrement=True,
                nullable=False)
    name = Column(String(128), nullable=False)
