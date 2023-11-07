#!/usr/bin/python3
"""append_file funtion module """


def append_write(filename="", text=""):
    """function wrtie text to the end of a file"""
    with open(filename, "a+", encoding='utf-8') as file:
        return file.write(text)
