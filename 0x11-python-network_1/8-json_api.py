#!/usr/bin/python3
""" send post req and print body if json """
import requests
from sys import argv

if __name__ == "__main__":
    q = {"q": "" if len(argv) == 1 else argv[1]}
    req = requests.post("http://0.0.0.0:5000/search_user", data=q)
    if '{' and '}' in req.text:
        json = req.json()
        if len(json) == 0:
            print("No result")
        else:
            print("[{}] {}".format(json.get("id"), json.get("name")))
    else:
        print("Not a valid JSON")
