#!/usr/bin/python3

"""Module contains a function that inserts a line of text to a file,
after each line containing a specific string (see example):"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file,
    after each line containing a specific string"""

    content = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            content.append(line)
            if search_string in line:
                content.append(new_string)

    with open(filename, 'w', encoding='utf-8') as file:
        file.write("".join(content))
