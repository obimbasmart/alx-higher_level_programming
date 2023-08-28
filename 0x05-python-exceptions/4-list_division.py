#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    ''' divides element by element 2 lists.
        Args:
            @my_list_1 & @my_list_2 can contain any type (integer, string, ..)
            @list_length can be bigger than the length of both lists
        Return:
            a new list (length = list_length) with all divisions
    '''
    new_list = []
    for idx in range(list_length):
        result = 0
        try:
            result = my_list_1[idx] / my_list_2[idx]
        except ZeroDivisionError:
            print('division by 0')
        except TypeError:
            print('wrong type')
        except IndexError:
            print('out of range')
        finally:
            new_list.append(result)
    return new_list
