#!/usr/bin/python3

Class Rectangle

class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, value):
        if type(value) == int and value >= 0:
            self.__height = value
        elif type(value) != int:
            raise NameError("height must be an integer")
        elif value < 0:
            raise NameError("height must be >= 0")
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) == int and value >= 0:
            self.__width = value
        elif type(value) != int:
            raise NameError("width must be an integer")
        elif value < 0:
            raise NameError("width must be >= 0")

    def area(self):
        return self.__height*self.__width

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            self.__perimeter = 0
        else:
            self.__perimeter = 2 * (self.__height + self.__width)
        return self.__perimeter