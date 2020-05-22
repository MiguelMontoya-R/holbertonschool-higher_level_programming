#!/usr/bin/python3
""" Split a string '.', '?', ':' 
"""


def text_indentation(text):
    """ Split a string text by '.', '?', ':'

    Arguments:
        text {str} -- tet to be indented

    Raises:
        TypeError: [description]
        TypeError: [description]
    """
    if type(text) != str:
        raise TypeError('text must be a string')
    elif text == None:
        raise TypeError('Text must be a string')
    else:
        for i in text:
            if i == '.' or i == '?' or i == ':':
                print('{}'.format(i))
                print()
            else:
                print('{}'.format(i), end="")
