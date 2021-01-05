#!/usr/bin/python3
class Square:
    """
    Square Class that holds size

    Attributes:
        __size (integer): the size of the square instance

    """
    def __init__(self, new_size=None):
        """
        Initializes a square of size new_size

        Args:
            new_size: the size for the new square instance

        """
        if new_size is not None:
            self.__size = new_size

