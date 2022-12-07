def square_matrix_simple(matrix=[]):
    '''  function that computes the square value of all integers of a matrix.

        Args:
            @matrix: 2-dimensional matrix
        Return:
            2-d matrix
    '''
    return [[val**2 for val in _list] for _list in matrix]
