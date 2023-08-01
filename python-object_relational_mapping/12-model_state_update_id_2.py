#!/usr/bin/python3
"""A script that lists all State objects from the database hbtn_0e_6_usa"""

from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
import sys
from model_state import Base, State

if __name__ == "__main__":
    """Create an engine"""
    engine = create_engine("mysql://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    # Ouvre une session
    session = Session(engine)

    # charge l'objet
    my_row = session.execute(select(State).filter_by(id=2)).scalar_one()

    # MAJ l'objet
    my_row.name = "New Mexico"

    session.commit()

    session.close()
