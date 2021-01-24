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
