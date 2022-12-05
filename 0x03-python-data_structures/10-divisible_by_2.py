#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    ''' function that finds the biggest integer of a list.

        :Args:
            @my_list: list of integers
        :Return: maximum value in @my_list
    '''
    return [num % 2 == 0 for num in my_list]
