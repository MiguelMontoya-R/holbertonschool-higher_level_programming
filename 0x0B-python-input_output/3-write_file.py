#!/usr/bin/python3
"""[summary]
"""


def write_file(filename="", text=""):
    """[summary]

    Keyword Arguments:
        filename {str} -- [description] (default: {""})
        text {str} -- [description] (default: {""})

    Returns:
        [type] -- [description]
    """
    with open(filename, mode='w', encoding='utf-8') as filename:
        return filename.write(text)
