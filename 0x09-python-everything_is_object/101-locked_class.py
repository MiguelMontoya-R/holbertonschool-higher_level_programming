#!/usr/bin/python3
""" User can only create instance first_name
"""


class LockedClass:
    """ using slots to store first_name only
    """
    __slots__ = ['first_name']
