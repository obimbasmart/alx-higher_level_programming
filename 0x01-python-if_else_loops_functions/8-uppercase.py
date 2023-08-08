#!/usr/bin/python3

def uppercase(str):
    '''function write a string in uppercase followed
       by new line

       :@str: a single character string
       :Return: None
    '''
    for char in str:
        char_num = ord(char)
        if char_num > 96 and char_num < 123:
            char_num -= 32

        print("{:c}".format(char_num), end='')
    print("{:s}".format(''), end='\n')
