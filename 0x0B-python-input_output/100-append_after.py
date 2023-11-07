#!/usr/bin/python3
"""append_after funtion module"""


def append_after(filename="", search_string="", new_string=""):
    """
        adds new_string after lins contain search string
    """
    s = ""
    with open(filename, encoding="utf-8") as file:
        while True:
            t = file.readline()
            if not t:
                break
            if search_string in t:
                t += new_string
            s += t
    with open(filename, "w+", encoding="utf-8") as file:
        file.write(s)
