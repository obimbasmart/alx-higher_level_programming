#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    '''
        function that prints x elements of a list

        Args:
            @my_list: list
        Return:
            the real number of elements printed
    '''
    for idx in range(x):
        try:
            var = my_list[idx]
            print(var, end='')
        except IndexError:
            print()
            return idx
    print()
    return (idx + 1)
