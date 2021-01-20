#!/usr/bin/python3
"""Write a class MyInt that inherits from int:"""


class MyInt(int):
    """A rebellious cousin of the integer class"""
    def __eq__(a, b):
        """REBELIOUS =="""
        if a < b or a > b:
            return True
        else:
            return False

    def __ne__(a, b):
        """REBELIOUS !="""
        if a < b or a > b:
            return False
        else:
            return True
