#!/usr/bin/python3
"""inherits_from function module"""


def inherits_from(obj, a_class):
    """obj is inhirated from oject"""
    return isinstance(obj, a_class) and type(obj) is not a_class
