#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    ''' prints an integer with "{:d}".format().
        Args:
            @value: of any type - str, int, list etc
        Return:
            True for successful print. False if not
    '''
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError) as err:
        sys.stderr.write("Exception: {}\n".format(err))
        return False
    else:
        return True
