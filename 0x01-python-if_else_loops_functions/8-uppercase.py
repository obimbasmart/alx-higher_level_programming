#!/usr/bin/python3

def uppercase(str):
    '''function prints a string in uppercase followed
       by new line

       :@str: a single character string
       :Return: None
    '''
    for char in str:
        if ord(char) > 96 and ord(char) < 123:
            char_num = ord(char) - 32
        else:
            char_num = ord(char)

        print("{:c}".format(char_num), end='')
    print("")
