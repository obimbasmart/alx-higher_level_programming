#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    ''' function that prints the first x elements of a list and only integers

        Args:
            @my_list: can contain any type (integer, string, etc.)
            @x: represents the number of elements to access in my_list
        Return:
            -the real number of integers printed
    '''
    nlen = 0
    for idx in range(x):
        var = my_list[idx]
        try:
            print("{:d}".format(var), end='')
        except (ValueError, TypeError):
            continue
        else:
            nlen += 1
    print()
    return (nlen)
