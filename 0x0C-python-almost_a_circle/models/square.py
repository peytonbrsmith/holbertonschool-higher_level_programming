#!/usr/bin/python3
"""Write the class Square that inherits from Rectangle:"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """initializes square class"""
        super(Square, self).__init__(size, size, x, y, id)

    def __str__(self):
        """Returns string representation of square object"""
        string = "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.width)
        return(string)

    def update(self, *args, **kwargs):
        """Updates the values of the given object"""
        if len(args) != 0:
            i = 1
            for arg in args:
                if i == 1:
                    self.id = arg
                elif i == 2:
                    self.size = arg
                elif i == 3:
                    self.x = arg
                elif i == 4:
                    self.y = arg
                i += 1
        elif len(kwargs) != 0:
            for arg in kwargs.keys():
                if arg == "id":
                    self.id = kwargs.get(arg)
                if arg == "size":
                    self.size = kwargs.get(arg)
                if arg == "x":
                    self.x = kwargs.get(arg)
                if arg == "y":
                    self.y = kwargs.get(arg)

    def to_dictionary(self):
        """returns dictionary version of square"""
        sqr_dict = {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
        return sqr_dict

    @property
    def size(self):
        """size property"""
        return self.width

    @size.setter
    def size(self, size):
        """
        sets size
        """
        self.width = size
        self.height = size
