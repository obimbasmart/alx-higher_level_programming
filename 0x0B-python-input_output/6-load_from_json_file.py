#!/usr/bin/python3

"""module contains function that creates an Object from a “JSON file”"""

import json


def load_from_json_file(filename):
    """create an object form json file"""
    with open(filename, mode='r', encoding='utf-8') as file:
        content = file.read()
        return json.loads(content.strip())
