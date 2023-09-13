#!/usr/bin/python3

"""module contains function that writes a string
to a file (utf-8)"""


def write_file(filename="", text=""):
    """write string to file (utf-8)

    Args:
        filename(string): path to file/new_file
        text(string): text content
    Return:
        size(int): number of characters written to file
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        return file.write(text)
