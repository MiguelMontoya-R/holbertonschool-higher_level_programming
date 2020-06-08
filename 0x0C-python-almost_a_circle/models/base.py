#!/usr/bin/python
"""Base class
"""


class Base:
    """ If id is None the value is passed, but if not nb_objects is passed
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
