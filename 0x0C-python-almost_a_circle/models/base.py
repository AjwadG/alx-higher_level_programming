#!/usr/bin/python3
"""base class module"""
import json
from os.path import exists


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
        ls = []
        if list_objs is not None:
            for a in list_objs:
                ls.append(a.to_dictionary())
        with open(name + ".json", "w+", encoding="utf-8") as file:
            file.write(Base.to_json_string(ls))

    @staticmethod
    def from_json_string(json_string):
        """"dict to json"""
        a = json_string
        if a is None or type(a) is not str or len(a) == 0:
            return "[]"
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """"crates new obj"""
        name = cls.__name__
        if name == "Rectangle":
            tmp = cls(1, 1, 1, 1)
        elif name == "Square":
            tmp = cls(1, 1, 1)
        else:
            return None
        tmp.update(**dictionary)
        return tmp

    @classmethod
    def load_from_file(cls):
        """"crates new obj from avlues in file"""
        name = cls.__name__ + ".json"
        if not exists(name):
            return
        with open(name, "r+", encoding="utf-8") as file:
            tmp = cls.from_json_string(file.read())
        ls = []
        for a in tmp:
            ls.append(cls.create(**a))
        return ls
