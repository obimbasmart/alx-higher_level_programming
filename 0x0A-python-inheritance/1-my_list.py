#!/usr/bin/python3

"""This module contains a class MyList that inherits from list"""


class MyList(list):
    """a class that inherits from list object"""

    def print_sorted(self):
        """prints the list (ascending sort)"""
        print(list(sorted(self)))
