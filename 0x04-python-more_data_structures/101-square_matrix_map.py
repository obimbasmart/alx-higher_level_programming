#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return (list(map(lambda _list: [i**2 for i in _list], matrix)))
