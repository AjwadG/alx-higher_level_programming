#!/usr/bin/python3
""" send post req and print vody """
import requests
from sys import argv

if __name__ == "__main__":
    req = requests.post(argv[1], data={"email": argv[2]}).text
    print(req)
