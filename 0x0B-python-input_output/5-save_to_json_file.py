#!/usr/bin/python3
"""save_to_json_file funtion module """
import json


def save_to_json_file(my_obj, filename):
    """write the json og obj to file"""
    with open(filename, "w+", encoding='utf-8') as file:
        file.write(json.dumps(my_obj))
