#!/usr/bin/python3
""""Defines a class that inherits from the BaseGeometry class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Defines a class that inherits from the BaseGeometry class"""
    def __init__(self, width, height):
        self.__width = BaseGeometry().integer_validator("width", width)
        self.__height = BaseGeometry().integer_validator("width", height)
