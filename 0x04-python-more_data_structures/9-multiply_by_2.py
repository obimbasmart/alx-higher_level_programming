#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    '''  returns a new dictionary with all values multiplied by 2
         Args:
            @a_dictionary: the initial dictionary
         Return:
            new dictionary
    '''
    return {key: val * 2 for key, val in a_dictionary.items()}
