#!/usr/bin/python3
"""Module of Rectangle"""


class Rectangle:
    """Represents a Rectangle"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """initilationg width, height values of Rectangle"""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    def __str__(self):
        """return a Rectangle of #"""
        if self.__width == 0 or self.__height == 0:
            return ''
        string = ''
        for i in range(self.__height):
            string += self.__width * str(self.print_symbol) + '\n'
        return string[:-1]

    def __repr__(self):
        """return a strin representing the Rectangle opject"""
        return "Rectangle("+str(self.__width)+", "+str(self.__height)+")"

    def __del__(self):
        """prints a message when del the opject"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @property
    def width(self):
        """gets the value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the value of width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """gets the value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the value of height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """area method return are of Rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """perimeter method return perimeter of Rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * 2 + self.__height * 2

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """static methos that compares the area of rect_1 and tow"""
        if type(rect_1) != Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) != Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """class method crates rect with widt and height of size"""
        return cls(size, size)
