#!/usr/bin/python3

def safe_print_integer(value):
    ''' prints an integer with "{:d}".format().
        Args:
            @value: of any type - str, int, list etc
        Return:
            True for successful print. False if not
    '''
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError):
        return False
    else:
        return True
