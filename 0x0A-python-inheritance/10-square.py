#!/usr/bin/python3
"""Rectangle class module"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square supclass of Rectangle"""
    def __init__(self, size):
        """init base values"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
