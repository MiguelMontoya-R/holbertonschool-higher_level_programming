#!/usr/bin/python3
"""[summary]
"""


def append_write(filename="", text=""):
    """[summary]

    Keyword Arguments:
        filename {str} -- [description] (default: {""})
        text {str} -- [description] (default: {""})

    Returns:
        [type] -- [description]
    """
    with open(filename, mode='a', encoding='utf-8') as filename:
        return filename.write(text)
