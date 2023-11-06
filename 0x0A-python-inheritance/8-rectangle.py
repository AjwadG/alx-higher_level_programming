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
