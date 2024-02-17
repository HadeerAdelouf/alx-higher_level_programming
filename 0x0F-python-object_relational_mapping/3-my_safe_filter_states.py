#!/usr/bin/python3
"""
Script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument
but safe from MySQL injections!
"""

import MySQLdb as db
from sys import argv

if __name__ == "__main__":
    """
    Access to the database and get the states
    from the database.
    """
    db_connect = db.connect(host="localhost", port=3306,
                            user=argv[1], passwd=argv[2], db=argv[3])

    db_cursor = db_connect.cursor()
    db_cursor.execute(
        "SELECT * FROM states WHERE name LIKE \
                    BINARY %(name)s ORDER BY states.id ASC", {'name': argv[4]})

    rows = db_cursor.fetchall()

    for i in rows:
        print(i)
