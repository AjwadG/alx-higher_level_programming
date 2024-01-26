#!/usr/bin/python3
""" get print body if error print code """
import urllib.request
from sys import argv

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(argv[1]) as req:
            print(req.read().decode("UTF-8"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
