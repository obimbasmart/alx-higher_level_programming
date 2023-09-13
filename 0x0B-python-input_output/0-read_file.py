#!/usr/bin/python3

"""This module contains a function that reads a text file (utf-8)
and print it to stdout"""


def read_file(filename=""):
    """read text file (utf-8) and print to stdout"""
    with open(filename, mode='r', encoding='utf-8') as file:
        for line in file:
            print(line, end='')
