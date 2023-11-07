#!/usr/bin/python3
"""class_to_json funtion module """


class Student:
    """Student object"""
    def __init__(self, first_name, last_name, age):
        """init funtion to asign values"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns a dict of the class with filter"""
        if attrs is not None:
            di = dict()
            for a in attrs:
                try:
                    di[a] = self.__dict__[a]
                except Exception:
                    pass
            return di
        return self.__dict__

    def reload_from_json(self, json):
        """swaps attribute with jsons attr"""
        if json is not None:
            for a in json:
                try:
                    self.__dict__[a] = json[a]
                except Exception:
                    pass
