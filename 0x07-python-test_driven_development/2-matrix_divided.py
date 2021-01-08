#!/usr/bin/python3
"""This module includes a single method that adds 2 integers"""


def matrix_divided(matrix, div):
    """
    ``matrix_divided`` - divides a matrix content's by an integer

    Arguments:
        matrix - the matrix of integers or floats
        div - the integer to divide by

    Returns:
        a new matrix with the results
    """
    if type(div) not in list([int, float]):
            raise TypeError("div must be a number")
    new_matrix = []
    mtx = []
    if isinstance(matrix, list) is False:
        raise \
            TypeError("matrix must be a matrix (list of lists) of integers/floats")
    try:
        columns = len(matrix[0])
    except (TypeError, IndexError):
        raise \
            TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        if len(row) != columns:
            raise TypeError("Each row of the matrix must have the same size")
        for item in row:
            if type(item) not in list([int, float]):
                raise TypeError\
                    ("matrix must be a matrix (list of lists) of integers/floats")
            else:
                mtx.append(round(int(item) / div, 2))
        new_matrix.append(mtx)
        mtx = []
    return new_matrix
