#!/usr/bin/python3
"""class_to_json funtion module """


class Student:
    """Student object"""
    def __init__(self, first_name, last_name, age):
        """init funtion to asign values"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns a dict of the funtion"""
        return self.__dict__
