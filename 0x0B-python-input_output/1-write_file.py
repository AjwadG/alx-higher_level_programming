#!/usr/bin/python3
"""write_file funtion module """


def write_file(filename="", text=""):
    """function wrtie text to file"""
    with open(filename, "w+", encoding='utf-8') as file:
        return file.write(text)
