#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    db_connect = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                                 passwd=sys.argv[2], db=sys.argv[3])
    db_cursor = db_connect.cursor()
    db_cursor.execute(
        "SELECT * FROM states WHERE name LIKE \
                    BINARY %(name)s ORDER BY states.id ASC", {'name': argv[4]})

    rows = db_cursor.fetchall()
    for i in rows:
        print(i)

    db_cursor.close()
    db_connect.close()
