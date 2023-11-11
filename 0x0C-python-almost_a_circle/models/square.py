#!/usr/bin/python3
"""Square class module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class sup from rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """class constructior"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """width getter"""
        return self.width

    @size.setter
    def size(self, value):
        """width setter"""
        self.width = value
        self.height = value

    def __str__(self):
        """returns formated string of the obj"""
        id = self.id
        size = self.width
        x = self.x
        y = self.y
        return "[Square] ({}) {}/{} - {}".format(id, x, y, size)
