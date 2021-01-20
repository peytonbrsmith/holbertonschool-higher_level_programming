#!/usr/bin/python3
"""Write a class Square that inherits from Rectangle (9-rectangle.py)"""
Rectangle = __import__('9-rectangle').Rectangle
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(Rectangle):
    """Square instance, inherits Rectangle"""
    def __init__(self, size):
        """Initiates a square class with private size + rectangle attributes"""
        BaseGeometry().integer_validator("size", size)
        super(Square, self).__init__(size, size)
        self.__size = size
