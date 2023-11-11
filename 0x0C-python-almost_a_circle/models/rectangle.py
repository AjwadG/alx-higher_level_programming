#!/usr/bin/python3
"""Rectangle class module"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class sup from base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """class constructior"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """calculates the rea of the rect"""
        return self.__width * self.__height

    def display(self):
        """prints shape out of #'s"""
        print('\n' * self.__y, end='')
        for i in range(self.__height):
            print(' ' * self.__x + '#' * self.__width)

    def __str__(self):
        """returns formated string of the obj"""
        id = self.id
        wi = self.width
        he = self.height
        x = self.x
        y = self.y
        return "[Rectangle] ({}) {}/{} - {}/{}".format(id, x, y, wi, he)

    def update(self, *args, **kwargs):
        """updates obj attrs"""
        if args is not None and len(args) != 0:
            a = len(args)
            if a >= 1:
                self.id = args[0]
            if a >= 2:
                self.width = args[1]
            if a >= 3:
                self.height = args[2]
            if a >= 4:
                self.x = args[3]
            if a >= 5:
                self.y = args[4]
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """returns the object as a dict"""
        return {"id": self.id, "width": self.width,
                "height": self.height, "x": self.x,
                "y": self.y}
