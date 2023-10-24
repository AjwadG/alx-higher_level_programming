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

    @property
    def size(self):
        """gets the value of size"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets the value of size"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """prints a square of #"""
        for i in range(self.__size):
            print(self.__size * '#')
        if self.__size == 0:
            print()
