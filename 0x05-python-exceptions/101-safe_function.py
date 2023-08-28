#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    ''' executes a function safely
        Args:
            @fct will be always a pointer to a function
        Return:
            the result of the function
    '''
    try:
        result = fct(*args)
    except Exception as e:
        sys.stderr.write("Exception: {}\n".format(e))
        return None
    else:
        return result
