#!/usr/bin/python3
"""load_from_json_file funtion module """
import json


def load_from_json_file(filename):
    """reads json from a file"""
    with open(filename, encoding='utf-8') as file:
        return json.loads(file.read())
