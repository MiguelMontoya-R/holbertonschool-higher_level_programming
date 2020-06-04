#!/usr/bin/python3
"""from json string

Returns:
    json.loads(my_str) -- String representation of json
"""
import json


def from_json_string(my_str):
    """from json string

    Arguments:
        my_str {str} -- Json string

    Returns:
        json.loads(my_str) -- String representation of json
    """
    return json.loads(my_str)
