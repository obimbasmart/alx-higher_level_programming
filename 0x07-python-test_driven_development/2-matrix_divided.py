""" This module contains a function that divides all elements of a matrix

 - Prototype: def matrix_divided(matrix, div):
 - matrix must be a list of lists of integers or floats, otherwise raise a
        TypeError exception with the message matrix must be a matrix
        (list of lists) of integers/floats
 - Each row of the matrix must be of the same size, otherwise
        raise a TypeError exception with the message Each row of
        the matrix must have the same size
 - div must be a number (integer or float), otherwise raise a
        TypeError exception with the message div must be a number
 - div can’t be equal to 0, otherwise raise a ZeroDivisionError
        exception with the message division by zero
 - All elements of the matrix should be divided by div,
        rounded to 2 decimal places
 - Returns a new matrix
 - You are not allowed to import any module
"""


def matrix_divided(matrix, div):
    """function divides all elements of a matrix

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
        return
    # check if matrix is a list of list
    for item in matrix:
        if not isinstance(item, list):
            raise TypeError("matrix must be a matrix"
                            " (list of lists) of integers/floats")
            return
    # check if matrix is a list of list of integers or float
    for item in matrix:
        for num in item:
            if not isinstance(num, (int, float)):
                raise TypeError("matrix must be a matrix "
                                "(list of lists) of integers/floats")
                return
    # Each row of the matrix must be of the same size
    size = len(matrix[0])
    for item in matrix:
        if len(item) != size:
            raise TypeError("Each row of the matrix must have the same size")
            return
    if div == 0:
        raise TypeError("division by zero")
        return
    new_matrix = []
    new_list = []
    for item in matrix:
        for num in item:
            new_list.append(round(num/div, 2))
        new_matrix.append(new_list)
        new_list = []

    return new_matrix
