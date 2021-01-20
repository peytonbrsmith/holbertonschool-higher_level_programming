#!/usr/bin/python3
""""Defines a class that inherits from the BaseGeometry class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Defines a class that inherits from the BaseGeometry class"""
    def __init__(self, width, height):
        BaseGeometry().integer_validator("width", width)
        self.__width = width
        BaseGeometry().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Method for returning the area of a rectangle instance"""
        return (self.__width * self.__height)

    def __str__(self):
        """Creates the string representation of a rectangle"""
        return("[Rectangle] {:d}/{:d}".format(self.__width, self.__height))
