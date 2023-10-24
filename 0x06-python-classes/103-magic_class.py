#!/usr/bin/python3
"""Module of Square"""
import math


class MagicClass:
    """Represents a Square, with a name."""
    def __init__(self, radius=0):
        """initilationg size value of Square"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """area method return are of square"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """area method return are of square"""
        return 2 * math.pi * self.__radius
