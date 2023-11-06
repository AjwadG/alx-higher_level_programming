#!/usr/bin/python3
"""lookup function module"""


def lookup(obj):
    """ lookup funtion checks the obj

        Args:
            obj: oject to chect its info

        Return:
            list of attributes and methods of obj
    """
    if not obj:
        return None
    return dir(obj)
