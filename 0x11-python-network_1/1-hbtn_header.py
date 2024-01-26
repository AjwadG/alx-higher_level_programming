#!/usr/bin/python3
""" prints the id of the res """
import urllib.request
from sys import argv

if __name__ == "__main__":
    with urllib.request.urlopen(argv[1]) as req:
        res = req.info()
        print(res.get("X-Request-Id"))
