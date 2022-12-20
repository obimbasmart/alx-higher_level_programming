#!/usr/bin/python3

def safe_print_division(a, b):
    '''  function that divides 2 integers and prints the result.

        Args:
            @a, @b - integers
        Return:
            -results of division
    '''
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        result = None
    finally:
        print("{}".format(result))
