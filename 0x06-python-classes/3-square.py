#!/usr/bin/python3
"""Module of Square"""


class Square:
    """Represents a Square, with a name."""
    def __init__(self, size=0):
        """initilationg size value of Square"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """area method return are of square"""
        return self.__size ** 2
