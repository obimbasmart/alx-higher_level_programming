#!/usr/bin/python3

"""This module contains implemenentation
of the Pascal triangle function"""


def pascal_triangle(n):
    """returns a list of lists of integers
    representing the Pascal’s triangle n:"""
    pascal_tri = []
    for i in range(1, n+1):
        pascal_tri.append(pascal_row(i))
    return pascal_tri


def pascal_row(n):
    """returns a list of integers
    representing the Pascal’s triangle of row n:"""
    row_n = []
    for i in range(n):
        row_n.append(comb(n - 1, i))
    return row_n


def fact(n):
    """return the factorial of a number: n"""
    if n == 0:
        return 1
    return n * fact(n - 1)


def comb(n, r):
    """return the combination of a number: n
    with given ratio: r"""
    return fact(n) // (fact(r) * fact(n - r))
