#!/usr/bin/python3

def weight_average(my_list=[]):
    '''  returns the weighted average of all
         integers tuple (<score>, <weight>)

         Args:
             @my_list: the ilist of interger tuple
         Return:
             integer: weighted average
    '''
    numerator = sum(list(map(lambda tup: tup[0] * tup[1], my_list)))
    denominator = sum(list(map(lambda tup: tup[1], my_list)))
    return numerator / denominator
