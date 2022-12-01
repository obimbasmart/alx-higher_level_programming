#!/usr/bin/python3

def islower(c):
    '''function checks for lowercase character

       :@c: a single character string
       :Return: True if is lowercase. False if not
    '''
    if ord(c) > 96 and ord(c) < 123:
        return (True)

    return (False)
