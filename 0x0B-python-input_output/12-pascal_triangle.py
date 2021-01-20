#!/usr/bin/python3
"""
Create a function def pascal_triangle(n): that returns a list of
lists of integers representing the Pascal’s triangle of n:
"""
from math import factorial


def bc(n, k):
    """calculates binomial coefficients"""
    return int((factorial(n)) / ((factorial(k)) * factorial(n - k)))


def pascal_triangle(n):
    """creates the triangle"""
    return_list = []
    new_list = []
    for row in range(n):
        for column in range(row + 1):
                new_list.append(bc(row, column))
        return_list.append(new_list)
        new_list = []
    return (return_list)
