#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    ''' function that prints a matrix of integers

        :Args:
        :Return: None
    '''
    for id_row in range(0, len(matrix)):  # for each row in matrix
        sep = ' '
        for id_col in range(0, len(matrix[id_row])):  # for each int in row
            if id_col == 2:
                sep = ''

            print("{:d}".format(matrix[id_row][id_col]), end=sep)
        print('')
