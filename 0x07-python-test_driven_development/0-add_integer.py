#!/usr/bin/python3
"""
Addition of two numbers
"""
def add_integer(a, b=98):
    """ Addition of two numbers

    Arguments:
        a {int} -- Number

    Keyword Arguments:
        b {int} -- Number (default: {98})

    Returns:
        [int] -- The addition of 'a' and 'b'
    """
    if type(a) not in [int, float]:
        raise TypeError('a must be an integer')
    elif type(b) not in [int, float]:
        raise TypeError('b must be an integer')
    return (a + b)
