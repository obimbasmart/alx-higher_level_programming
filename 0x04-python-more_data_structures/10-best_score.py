#!/usr/bin/python3

def best_score(a_dictionary):
    '''  returns a key with the biggest integer value.
         Args:
            @a_dictionary: the initial dictionary
         Return:
            new dictionary
    '''
    if not a_dictionary:
        return None

    best_score = max(set(a_dictionary.values()))
    for key, val in a_dictionary.items():
        if val == best_score:
            return key

    return None
