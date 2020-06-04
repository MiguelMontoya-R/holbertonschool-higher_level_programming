#!/usr/bin/python3
"""[summary]

Returns:
    [type] -- [description]
"""
import json


def save_to_json_file(my_obj, filename):
    """[summary]

    Arguments:
        my_obj {[type]} -- [description]
        filename {[type]} -- [description]

    Returns:
        [type] -- [description]
    """
    with open(filename, 'w') as filename:
        return filename.write(json.dumps(my_obj))
