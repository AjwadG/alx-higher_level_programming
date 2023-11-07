#!/usr/bin/python3
"""from_json_string funtion module """
import json


def from_json_string(my_str):
    """converts string to object"""
    return json.loads(my_str)
