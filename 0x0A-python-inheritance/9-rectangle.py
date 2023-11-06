#!/usr/bin/python3
"""Rectangle class module"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle supclass of BaseGeometry"""
    def __init__(self, width, height):
        """init base values"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """returns the area of the rect"""
        return self.__width * self.__height

    def __str__(self):
        """returns the rect in format string"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
