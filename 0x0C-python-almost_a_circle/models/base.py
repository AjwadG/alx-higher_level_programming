#!/usr/bin/python3
"""base class module"""


class Base:
    """base class for all shapes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructior"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
