#!/usr/bin/python3
"""add_attribute function module"""


def add_attribute(obj, key, value):
    """tries to add aa new attribute to obj"""
    if hasattr(obj, "__dict__"):
        setattr(obj, key, value)
    else:
        raise TypeError("can't add new attribute")
