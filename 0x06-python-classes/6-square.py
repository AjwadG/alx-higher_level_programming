#!/usr/bin/python3
"""Module of Square"""


class Square:
    """Represents a Square, with a name."""
    def __init__(self, size=0, position=(0, 0)):
        """initilationg size value of Square"""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """gets the value of size"""
        return self.__position

    @position.setter
    def position(self, value):
        """sets the value of position"""
        if (not isinstance(value, tuple) or len(value) != 2 or type(value[0])
                != int or type(value[1]) != int or value[1] < 0 or
                value[0] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """prints a square of #"""
        if self.__size == 0:
            print()
            return
        print(self.__position[1] * '\n', end='', sep='')
        for i in range(self.__size):
            print(self.__position[0] * ' ', self.__size * '#', sep='')
