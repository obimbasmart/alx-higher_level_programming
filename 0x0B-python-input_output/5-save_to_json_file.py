#!/usr/bin/python3

"""This module contains a function that writes
an Object to a text file, using a JSON representation:"""

import json


def save_to_json_file(my_obj, filename):
    """write object to text file, using JSON"""
    with open(filename, mode='w', encoding='utf-8') as file:
        json.dump(my_obj, file)
