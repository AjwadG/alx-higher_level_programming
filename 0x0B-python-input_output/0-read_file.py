#!/usr/bin/python3
"""read_file funtion module """


def read_file(filename=""):
    """function prints all content of a file"""
    with open(filename, encoding='utf-8') as file:
        print(file.read(), end="")
