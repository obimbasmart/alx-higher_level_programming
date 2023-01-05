#!/usr/bin/python3

"""
Write a function that prints a text with 2 new lines
after each of these characters: ., ? and :

- Prototype: def text_indentation(text):
- text must be a string, otherwise raise a TypeError exception
    with the message text must be a string
- There should be no space at the beginning or at the end of each
    printed line
- You are not allowed to import any module
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
