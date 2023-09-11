#!/usr/bin/python3

"""
A class to demonstrate attribute constraint using python __slot__ attr
"""


class LockedClass:
    """a locked class preventing dynamic instance attr creation"""

    __slots__ = ("first_name")
