#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    '''  replaces or adds key/value in a dictionary.

         Args:
            @a_dictionary: the initial dictionary
            @key: assume that key is alwasys a string
            @value: value can be any type
         Return:
            new dictionary
    '''
    a_dictionary[key] = value
    return a_dictionary
