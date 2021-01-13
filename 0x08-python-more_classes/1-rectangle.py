#!/usr/bin/python3
"""Module containing Rectangle class and methods"""


class Rectangle:
    """

    Class that defines a rectangle

    Attributes:
        Height - height of the rectangle
        Width - width of the rectangle

    """
    def __init__(self, new_width=0, new_height=0):
        """
        Initializes a rectangle class instance
        Args:
            new_width - the new width
            new_height - the new height
        """
        self.height = new_height
        self.width = new_width

    @property
    def width(self):
        """Getter for the width property"""
        return self.__width

    @property
    def height(self):
        """Getter for the height property"""
        return self.__height

    @width.setter
    def width(self, new_width):
        """

        Setter for the width size of a rectangle class

        Args:
            new_width - the new width size

        """
        if isinstance(new_width, int) is True:
            if new_width >= 0:
                self.__width = new_width
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

    @height.setter
    def height(self, new_height):
        """

        Setter for the height size of a rectangle class

        Args:
            new_height - the new height size

        """
        if isinstance(new_height, int) is True:
            if new_height >= 0:
                self.__height = new_height
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")
