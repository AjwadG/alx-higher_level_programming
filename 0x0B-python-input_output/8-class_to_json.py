#!/usr/bin/python3
"""class_to_json funtion module """


def class_to_json(obj):
    """converts obj to dict"""
    return obj.__dict__
