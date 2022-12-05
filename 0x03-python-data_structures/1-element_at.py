#!/usr/bin/python3
def element_at(my_list, idx):
    '''function that retrieves an element from a list like in C

       Args:
            :my_list -  a list
            :idx - the element index

       Return:
            :element at position idx or None if none exist
    '''
    if (idx < 0 or idx > len(my_list) - 1):
        return None

    return my_list[idx]
