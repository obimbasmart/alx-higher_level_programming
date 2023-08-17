#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    '''  deletes a key in a dictionary.
         Args:
            @a_dictionary: the initial dictionary
            @key: assume that key is alwasys a string
         Return:
            new dictionary
    '''
    if key in a_dictionary.keys():
        del a_dictionary[key]

    return a_dictionary
