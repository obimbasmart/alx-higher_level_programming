#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    '''  returns a set of all elements present in only one set.

         Args:
            @set_1: the first set
            @set_2: the second set
         Return:
            A set
    '''
    return set_1 ^ set_2
