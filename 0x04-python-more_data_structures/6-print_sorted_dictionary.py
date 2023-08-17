#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    '''  prints a dictionary by ordered keys..

         Args:
            @a_dictionary
         Return:
            None
    '''
    a_dictionary = dict(sorted(a_dictionary.items()))
    for key in a_dictionary.keys():
        print("{:s}: {}".format(key, a_dictionary[key]))
