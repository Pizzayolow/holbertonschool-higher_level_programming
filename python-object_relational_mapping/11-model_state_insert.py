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

    # Créer l'objet name_db
    name_db = State(name="Louisiana")
    # Ouvre une session
    session = Session(engine)
    # Insert le name
    session.add(name_db)
    # Commit les changements
    session.commit()

    print(name_db.id)
    """Close the session"""
    session.close()
