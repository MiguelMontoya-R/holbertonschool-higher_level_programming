#!/usr/bin/python
import json
"""Base class
"""


class Base:
    """ If id is None the value is passed, but if not nb_objects is passed
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Base class

        Args:
            id ([type], optional): id parent. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """Returns JSON string representation

        Args:
            list_dictionaries: List of dictionaries to be represented in JSON
            string
        """
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        else:
            return '[]'
