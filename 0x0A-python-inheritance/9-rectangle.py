#!/usr/bin/python3


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):

    def __init__(self, width, height):
        self.integer_validator("height", height)
        self.integer_validator("width", width)
        self.__height = height
        self.__width = width

    def __str__(self):
        return str("[{}] {}/{}".format(self.__class__.__name__,
                                       self.__width, self.__height))

    def area(self):
        return self.__width * self.__height
