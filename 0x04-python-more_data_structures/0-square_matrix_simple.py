#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """compute the square value of all integers in a matrix
    Args:
        2-d matrix
    Return:
        2-d matrix
    """
    return [[num ** 2 for num in row] for row in matrix]
