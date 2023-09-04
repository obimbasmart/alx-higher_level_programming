#!/usr/bin/python3

"""
This module contains a function that multiplies 2 matrices:
"""


def matrix_mul(m_a, m_b):
    """multiply two matrix"""
    # check if args are lists
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    # check if args are lists of list
    check_type(m_a, "m_a must be a list of lists")
    check_type(m_b, "m_b must be a list of lists")

    # check if args are empty list
    is_empty(m_a, "m_a can't be empty")
    is_empty(m_b, "m_b can't be empty")

    # check if args contains list of integers or float
    check_nums(m_a, "m_a should contain only integers or floats")
    check_nums(m_b, "m_b should contain only integers or floats")

    # check if args are rectangle
    check_rows(m_a, "each row of m_a must be of the same size")
    check_rows(m_b, "each row of m_b must be of the same size")

    # check if m_a and m_b can be multiplied
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = []
    msum = 0
    for i in range(len(m_a)):
        my_list = []
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                msum += m_a[i][k] * m_b[k][j]
            my_list.append(msum)
            msum = 0
        result.append(my_list)

    return result


def check_type(matrix, err_msg):
    """check if matrix is a list of list"""
    for item in matrix:
        if not isinstance(item, list):
            raise TypeError(err_msg)


def is_empty(matrix, err_msg):
    """check if matrix is empty"""
    if not matrix or not matrix[0]:
        raise ValueError(err_msg)


def check_nums(matrix, err_msg):
    """checks if a matrix contains a list of list of integers"""
    for _list in matrix:
        for item in _list:
            if not isinstance(item, (int, float)):
                raise TypeError(err_msg)


def check_rows(matrix, err_msg):
    """check if matrix is a rectangle
    i.e all rows must be the same length
    """
    size = len(matrix[0])
    for _list in matrix:
        if size != len(_list):
            raise TypeError(err_msg)
