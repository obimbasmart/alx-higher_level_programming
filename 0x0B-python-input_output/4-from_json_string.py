#!/usr/bin/python3

"""module contains function that returns
 object representation of a JSON string"""
import json


def from_json_string(my_str):
    """returns object represented by JSON string
    i.e from json to object"""
    return json.loads(my_str)
