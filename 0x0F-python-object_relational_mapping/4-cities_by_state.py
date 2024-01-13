#!/usr/bin/python3
""" filter_states using MySQLdb"""
import MySQLdb
from sys import argv
host = "localhost"


def main():
    db = MySQLdb.connect(host=host, user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM states\
                 JOIN cities ON cities.state_id = states.id ORDER BY\
                 cities.id")

    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
