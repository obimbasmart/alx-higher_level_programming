#!/usr/bin/python3

def remove_char_at(str, n):
    """ remove character at position n"""
    str_copy = ""
    i = 0
    for char in str:
        if i == n:
            i += 1
            continue

        str_copy += char
        i += 1

    return (str_copy)
