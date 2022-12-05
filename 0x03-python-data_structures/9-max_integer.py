#!/usr/bin/python3

def max_integer(my_list=[]):
    ''' function that finds the biggest integer of a list.

        :Args:
            @my_list: list of integers
        :Return: maximum value in @my_list
    '''
    if len(my_list) == 0:
        return None

    _max = float('-inf')
    for num in my_list:
        if num > _max:
            _max = num

    return _max
