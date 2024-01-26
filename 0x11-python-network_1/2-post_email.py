#!/usr/bin/python3
""" send post req and print body """
import urllib.request
from sys import argv

if __name__ == "__main__":
    mail = urllib.parse.urlencode({"email": argv[2]}).encode('ascii')
    req_b = urllib.request.Request(argv[1], mail)
    with urllib.request.urlopen(req_b) as req:
        print(req.read().decode("UTF-8"))
