#!/usr/bin/python3

"""This is a script that adds all arguments to a Python list,
and then save them to a file:"""

import json
import sys
import os
load_from_json = __import__('6-load_from_json_file').load_from_json_file
save_to_json = __import__('5-save_to_json_file').save_to_json_file

file_name = 'add_item.json'


def add_all_args():
    # check if path exist
    if not os.path.exists(file_name):
        save_to_json([], file_name)

    my_list = load_from_json(file_name)
    my_list = my_list + sys.argv[1:]
    save_to_json(my_list, file_name)


if __name__ == "__main__":
    add_all_args()
