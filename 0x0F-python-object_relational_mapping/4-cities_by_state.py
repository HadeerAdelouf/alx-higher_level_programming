#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa
"""
import MySQLdb as db
from sys import argv

if __name__ == '__main__':
    db = MySQldb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    db_cur = db.cursor()
    db_cur.execute("SELECT cities.id, cities.name, states.name \
                                FROM cities JOIN states ON cities.state_id \
                                = states.id ORDER BY cities.id ASC")

    rows = db_cur.fetchall()
    for x in rows:
        print(x)
