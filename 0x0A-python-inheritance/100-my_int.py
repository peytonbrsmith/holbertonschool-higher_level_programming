#!/usr/bin/python3
"""Write a class MyInt that inherits from int:"""


class MyInt(int):
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
