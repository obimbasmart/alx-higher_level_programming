#!/usr/bin/python3

def search_replace(my_list, search, replace):
    ''' replaces all occurrences of an element by another in a new list..

        Args:
            @my_list: the initial list
            @search: the element to replace in the original list
            @replace: the new element
        Return:
            1-d array
    '''
    return [val if val != search else replace for val in my_list]
