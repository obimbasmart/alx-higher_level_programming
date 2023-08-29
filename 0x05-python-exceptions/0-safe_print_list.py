#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    '''
        prints x elements of a list
        Args:
            @my_list: list
        Return:
            number of elements printed
    '''
    if (x == 0 or not my_list):
        print()
        return (0)

    for idx in range(x):
        try:
            var = my_list[idx]
        except (IndexError, TypeError):
            print()
            return idx
        else:
            print(var, end='')

    print()
    return (idx + 1)
