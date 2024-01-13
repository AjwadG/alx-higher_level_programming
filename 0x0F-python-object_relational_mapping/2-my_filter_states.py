#!/usr/bin/python3
""" filter_states using MySQLdb"""
import MySQLdb
from sys import argv
host = "localhost"


def main():
    db = MySQLdb.connect(host=host, user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    comand = "SELECT * FROM states WHERE name LIKE BINARY '{}' \
                ORDER BY id ASC;".format(argv[4])
    cur.execute(comand)

    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
