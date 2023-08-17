#!/usr/bin/python3

def uniq_add(my_list=[]):
    ''' adds all unique integers in a list (only once for each integer).

        Args:
            @my_list: the initial list
        Return:
            sum of unique elements
    '''
    return sum(set(my_list))
