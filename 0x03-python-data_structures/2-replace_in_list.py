#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    '''function that replaces an element of a list at a specific position

       Args:
            :my_list -  a list
            :idx - the element index

       Return:
            :modified version of the list
    '''
    if (idx < 0 or idx > len(my_list) - 1):
        return my_list

    my_list[idx] = element
    return my_list
