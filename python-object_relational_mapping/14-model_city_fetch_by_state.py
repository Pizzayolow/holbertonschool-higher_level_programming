#!/usr/bin/python3
"""A script that lists all State objects from the database hbtn_0e_6_usa"""

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import sys
from model_state import Base, State
from model_city import Base, City

if __name__ == "__main__":
    engine = create_engine("mysql://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    # OUVRE LA SESSION
    session = Session(engine)

    # RECUPERER LES OBJETS
    villes = session.query(State, City).join(City, 
        City.state_id == State.id).order_by(City.id).all()

    for el1, el2 in villes:
        print(f"{el1.name}: ({el2.id}) {el2.name}")
