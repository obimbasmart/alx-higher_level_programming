#!/usr/bin/python3

"""
This module contans function for priting text with indentations
"""


def text_indentation(text):
    """ function that prints a text with 2 new lines
    after each of these characters: ., ? and :

    Args:
        text(string): text character
    Returns:
        nothing
    """
    # check if text is string
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    is_new_line = 0

    for char in text:
        if char in "?.:":
            print("\n")
            is_new_line = 1
        else:
            if char == ' ' and is_new_line:
                continue
            print(char, end="")
            is_new_line = 0
