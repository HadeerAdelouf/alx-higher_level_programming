#!/usr/bin/python3
"""
This script lists all states from the
database `hbtn_0e_0_usa` with a name starting with N.
"""

import MySQLdb
import sys

if __name__ == '__main__':
    db_connect = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                                 passwd=sys.argv[2], db=sys.argv[3])
    db_cursor = db_connect.cursor()
    db_cursor.execute("SELECT * FROM states WHERE name\
                LIKE BINARY 'N%' ORDER BY id ASC")
    rows = db_cursor.fetchall()
    for i in rows:
        print(i)

    db_cursor.close()
    db_connect.close()
