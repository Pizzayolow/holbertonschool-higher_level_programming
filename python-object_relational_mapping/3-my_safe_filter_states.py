#!/usr/bin/python3
"""A script that lists all states from the database hbtn_0e_0_usa"""

from sqlalchemy import create_engine, text
import sys

if __name__ == "__main__":
    user = sys.argv[1]
    passwd = sys.argv[2]
    dbname = sys.argv[3]
    state_name = sys.argv[4]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306\
        /{}'.format(user, passwd, dbname))

    with engine.connect() as connection:
        query = text('SELECT * FROM states WHERE BINARY name = :value \
            ORDER BY states.id ASC')

        result = connection.execute(query, {"value":state_name})

        for row in result:
            print(row)
