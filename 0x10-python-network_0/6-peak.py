#!/usr/bin/python3
"""find the peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """find peak"""
    if not list_of_integers or len(list_of_integers) < 3:
        return None

    for i in range(1, (len(list_of_integers) // 2) + 2):
        right = list_of_integers[i + 1]
        left = list_of_integers[i - 1]
        if all(list_of_integers[i] > niegbor for niegbor in (left, right)) or \
                (left == right and len(list_of_integers) == 3):
            return list_of_integers[i]

    return list_of_integers[0]
