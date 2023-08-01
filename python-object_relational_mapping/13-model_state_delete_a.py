#!/usr/bin/python3
"""A script that lists all State objects from the database hbtn_0e_6_usa"""

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import sys
from model_state import Base, State

if __name__ == "__main__":
    """Create an engine"""
    engine = create_engine("mysql://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    """Create a session"""
    session = Session(engine)

    """Query the database and format output"""
    s = session.query(State).filter(State.name.like('%a%')).order_by(State.id)

    for row in s:
        session.delete(row)

    session.commit()

    """Close the session"""
    session.close()
