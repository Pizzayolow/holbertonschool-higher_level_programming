#!/usr/bin/python3
"""A script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = db.cursor()
    cursor.execute(
        """
        SELECT GROUP_CONCAT(cities.name SEPARATOR ', ')
        AS cities
        FROM cities
        LEFT JOIN states
        ON states.id=cities.state_id
        WHERE states.name=%s
        ORDER BY cities.id
        """, (sys.argv[4],),
    )

    rows = cursor.fetchone()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
