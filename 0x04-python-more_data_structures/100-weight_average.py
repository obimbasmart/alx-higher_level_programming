#!/usr/bin/python3

def weight_average(my_list=[]):
    '''  returns the weighted average of all
         integers tuple (<score>, <weight>)

         Args:
             @my_list: the ilist of interger tuple
         Return:
             integer: weighted average
    '''
    if not my_list:
        return 0

    return sum([tup[0] * tup[1] for tup in my_list]) /
    sum([tup[1] for tup in my_list])
