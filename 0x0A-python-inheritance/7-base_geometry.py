#!/usr/bin/python3
"""BaseGeometry class module"""


class BaseGeometry:
    """BaseGeometry only to couse trouple"""
    def area(self):
        """rises error"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """checks if value is int"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
