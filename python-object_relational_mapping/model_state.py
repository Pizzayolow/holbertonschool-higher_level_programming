"""Base class"""
from sqlalchemy import Column, Integer, String, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, text
Base = declarative_base()


class State(Base):
    """class base"""
    __tablename__ = 'states'
    id = Column(Integer,
                Unique=True,
                primary_key=True,
                autoincrement=True,
                nullable=True)
    name = Column(String(128), nullable=True)
