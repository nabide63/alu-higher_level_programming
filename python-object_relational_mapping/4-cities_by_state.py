#!/usr/bin/python3
""" 4-cities_by_state.py """


import MySQLdb
import sys


def select_cities():
    """ lists all cities from the database
    """
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3]
                         )
    cur = db.cursor()

    cur.execute("SELECT cities.id, cities.name, \
        states.name FROM cities\
        JOIN states ON cities.state_id = states.id\
        ORDER BY cities.id ASC")

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    select_cities()
