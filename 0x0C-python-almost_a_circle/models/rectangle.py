#!/usr/bin/python3
"""Write the class Rectangle that inherits from Base:"""

from models.base import Base

class Rectangle(Base):
    """
    Class Rectangle inherits from Base
        Private instance attributes, each with its own public getter
        and setter:
            __width -> width
            __height -> height
            __x -> x
            __y -> y
    Class constructor: def __init__(self, width, height, x=0, y=0, id=None):
            Call the super class with id - this super call with use the
            logic of the __init__ of the Base class
            Assign each argument width, height, x and y to the right attribute
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a rectangle class instance based of Base
        """
        super(Rectangle, self).__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """property that returns private instance attribute width"""
        return self.__width

    @property
    def height(self):
        """property that returns private instance attribute height"""
        return self.__height

    @property
    def x(self):
        """property that returns private instance attribute x"""
        return self.__x

    @property
    def y(self):
        """property that returns private instance attribute y"""
        return self.__y

    @width.setter
    def width(self, width):
        """
        sets width
        """
        self.__width = width

    @height.setter
    def height(self, height):
        """
        sets height
        """
        self.__height = height

    @x.setter
    def x(self, x):
        """
        sets x
        """
        self.__x = x

    @y.setter
    def y(self, y):
        """
        sets y
        """
        self.__y = y
