#!/usr/bin/python3
""" filter_cities using MySQLdb"""
import MySQLdb
from sys import argv
host = "localhost"


def main():
    db = MySQLdb.connect(host=host, user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM states JOIN cities ON\
                 cities.state_id = states.id WHERE states.name\
                 LIKE BINARY %s ORDER BY cities.id;", (argv[4],))

    rows = cur.fetchall()
    for i in range(len(rows)):
        if i < len(rows) - 1:
            print(rows[i][0], end=", ")
        else:
            print(rows[i][0], end='')
    print()
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
