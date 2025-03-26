#!/usr/bin/python3
""" 5-filter_cities.py """

import MySQLdb
import sys


def my_safe_filter_states():
    """ lists all cities from the database
    """

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3]
                         )
    cur = db.cursor()

    sql = "SELECT cities.name FROM cities\
            JOIN states ON cities.state_id = states.id\
            AND states.name = %s\
            ORDER BY cities.id ASC"

    cur.execute(sql, (sys.argv[4],))

    rows = cur.fetchall()
    cites = []

    for row in rows:
        cites.append(row[0])

    print(", ".join(cites))
    cur.close()
    db.close()


if __name__ == "__main__":
    my_safe_filter_states()
