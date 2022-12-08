#!/usr/bin/python3

def multiply_list_map(my_list=[], number=0):
    '''  returns a list with all values multiplied by a
         number without using any loops.

         Args:
            @a_dictionary: the initial dictionary
            @number: the number to multiply with
         Return:
            list
    '''
    return list(map(lambda x: x * number, my_list))
