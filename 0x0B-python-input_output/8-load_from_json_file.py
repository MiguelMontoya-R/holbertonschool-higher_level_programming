#!/usr/bin/python3
"""[summary]

Returns:
    [type] -- [description]
"""
import json


def load_from_json_file(filename):
    """[summary]

    Arguments:
        filename {[type]} -- [description]

    Returns:
        [type] -- [description]
    """
    with open(filename, mode='r', encoding='utf-8') as f:
        return json.load(f)
