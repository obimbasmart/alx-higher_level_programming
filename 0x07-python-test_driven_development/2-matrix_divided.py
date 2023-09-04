#!/usr/bin/python3

""" This module contains a function that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """divides all elements of a matrix

    Args:
        matrix(list): a list of list
        div(int): a number greater than 0
    Return:
        a new matrix(list) of elements after division
"""
    # check if matrix is a list
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix "
                        "(list of lists) of integers/floats")

    # check if matrix is empty
    if matrix == []:
        return []

    # check if matrix is a list of list
    if not all([isinstance(item, list) for item in matrix]):
        raise TypeError("matrix must be a matrix "
                        "(list of lists) of integers/floats")

    # check if matrix is a list of list of integers or float
    for item in matrix:
        if not all([isinstance(num, (int, float)) for num in item]):
            raise TypeError("matrix must be a matrix "
                            "(list of lists) of integers/floats")

    # Each row of the matrix must be of the same size
    size = len(matrix[0])
    for item in matrix:
        if len(item) != size:
            raise TypeError("Each row of the matrix must have the same size")

    # check if div is a number
    if not isinstance(div, (float, int)):
        raise TypeError("div must be a number")

    # check for division by 0
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(num / div, 2) for num in item] for item in matrix]
    return new_matrix
