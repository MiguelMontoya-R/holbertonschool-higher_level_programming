#!/usr/bin/python3
"""Function of obj and classes
"""


def is_same_class(obj, a_class):
    """ function that returns True if the object is
        exactly an instance of the specified class;
        otherwise False.

    Args:
        obj ([type]): object type
        a_class ([type]): object's class or type()

    Returns:
        True: if is instance
        False: Otherwise
    """
    if type(obj) == a_class:
        return True
    else:
        return False
