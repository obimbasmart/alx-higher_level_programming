#!/usr/bin/python3

"""module contains function that appends a string
at the end of a file (utf-8)"""


def append_write(filename="", text=""):
    """append string to file (utf-8)

    Args:
        filename(string): path to file/new_file
        text(string): text content
    Return:
        size(int): number of characters appended to file
    """
    with open(filename, mode='a', encoding='utf-8') as file:
        return file.write(text)
