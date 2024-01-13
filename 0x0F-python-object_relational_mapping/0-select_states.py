#!/usr/bin/python3
""" select_states using MySQLdb"""
import MySQLdb
from sys import argv
host = "localhost"


def main():
    db = MySQLdb.connect(host=host, user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id;")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
