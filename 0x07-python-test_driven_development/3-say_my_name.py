#!/usr/bin/python3
""" Function that prints the name and the last name
of the person
"""


def say_my_name(first_name, last_name=""):
    """Function that prints the name and the last name
of the person
    Arguments:
        first_name {string} -- Frist Name

    Keyword Arguments:
        last_name {str} -- Last Name (default: {""})
    """
    if type(first_name) != str:
        raise TypeError('first_name must be a string')
    elif type(last_name) != str:
        raise TypeError('last_name must be a string')
    else:
        print('My name is {} {}'.format(first_name, last_name))
