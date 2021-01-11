#!/usr/bin/python3
"""Module containing Rectangle class and methods"""


class Rectangle:
    """

    Class that defines a rectangle

    Class Attributes:
        number_of_instances - the number of Rectangle instances in
        the current scope
        print_symbol - the symbol to print with

    Instance Attributes:
        Height - height of the rectangle
        Width - width of the rectangle

    Methods:
        Area- calculates the area
        Perimeter - calculates the perimeter

    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, new_width=0, new_height=0):
        """
        Initializes a rectangle class instance
        Args:
            new_width - the new width
            new_height - the new height
        """
        self.height = new_height
        self.width = new_width
        Rectangle.number_of_instances += 1

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

    def area(self):
            """Returns the area of the rectangle"""
            return (self.height * self.width)

    def perimeter(self):
            """Returns the perimeter of the rectangle"""
            if self.height is 0 or self.width is 0:
                return 0
            return ((self.height * 2) + (self.width * 2))

    def __str__(self):
        """creates the Rectangle's string used by the print() function"""
        string = ""
        if self.perimeter == 0:
            return string
        else:
            for i in range(self.height):
                for i in range(self.width):
                    string += str(self.print_symbol)
                string += "\n"
        return string[:-1]

    def __repr__(self):
        """
        Returns a string representation of the class in a format
        that can be used with eval() to create an identical instance
        """
        return ("Rectangle({}, {})".format(self.width, self.height))

    def __del__(self):
        """This is the deletion method of a Rectangle class"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compares rectangle instances based on area"""
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if (rect_2.area()) > (rect_1.area()):
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        """Creates a square Rectangle instance"""
        return cls(size, size)
