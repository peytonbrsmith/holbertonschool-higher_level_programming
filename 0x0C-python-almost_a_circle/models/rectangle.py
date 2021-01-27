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

    def area(self):
        """Returns the area of the rectangle"""
        return self.width * self.height

    def display(self):
        """Displays the rectangle in stdout with #s"""
        for rowspc in range(self.y):
                print()
        for row in range(self.height):
            for colspc in range(self.x):
                print(" ", end="")
            for col in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """Returns string representation of rec object"""
        string = "[Rectangle] ({}) {}/{} - {}/{}"\
            .format(self.id, self.x, self.y, self.width, self.height)
        return(string)

    def update(self, *args, **kwargs):
        """Updates the values of the given object"""
        if len(args) != 0:
            i = 1
            for arg in args:
                if i == 1:
                    self.id = arg
                elif i == 2:
                    self.width = arg
                elif i == 3:
                    self.height = arg
                elif i == 4:
                    self.x = arg
                elif i == 5:
                    self.y = arg
                i += 1
        elif len(kwargs) != 0:
            for arg in kwargs.keys():
                if arg == "id":
                    self.id = kwargs.get(arg)
                if arg == "width":
                    self.width = kwargs.get(arg)
                if arg == "height":
                    self.height = kwargs.get(arg)
                if arg == "x":
                    self.x = kwargs.get(arg)
                if arg == "y":
                    self.y = kwargs.get(arg)

    def to_dictionary(self):
        """returns a dictionary for itself"""
        rec_dict = {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
        return rec_dict

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
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @height.setter
    def height(self, height):
        """
        sets height
        """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @x.setter
    def x(self, x):
        """
        sets x
        """
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @y.setter
    def y(self, y):
        """
        sets y
        """
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y
