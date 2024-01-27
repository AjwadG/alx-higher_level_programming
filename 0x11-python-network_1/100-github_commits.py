#!/usr/bin/python3
""" github commits"""
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(argv[2], argv[1])
    limit = {"per_page": 10}
    header = {"X-GitHub-Api-Version": "2022-11-28"}

    req = requests.get(url, params=limit, headers=header).json()
    for commit in req:
        print("{}: {}".format(commit.get("sha"),
                              commit.get("commit").get("author").get("name")))
