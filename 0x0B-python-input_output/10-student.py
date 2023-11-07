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
