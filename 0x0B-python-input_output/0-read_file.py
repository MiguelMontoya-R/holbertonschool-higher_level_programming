#!/usr/bin/python3
"""[summary]
"""


def read_file(filename=""):
    """[summary]

    Keyword Arguments:
        filename {str} -- [description] (default: {""})
    """
    with open(filename, 'r') as f:
        for line in f:
            print(line, end="")
