#!/usr/bin/python3
"""base class module"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """"dict to json"""
        a = list_dictionaries
        if a is None or type(a) is not list or len(a) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """"dict to file"""
        name = cls.__name__
        with open(name + ".json", "w+", encoding="utf-8") as file:
            file.write(Base.to_json_string(list_objs))


