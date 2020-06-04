#!/usr/bin/python3
"""[summary]
"""


def number_of_lines(filename=""):
    """[summary]

    Keyword Arguments:
        filename {str} -- [description] (default: {""})

    Returns:
        [type] -- [description]
    """
    i = 0
    with open(filename, 'r') as f:
        for line in f:
            i += 1
        return i
