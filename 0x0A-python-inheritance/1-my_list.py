#!/usr/bin/python3
""" Print a list in sorted order
"""


class MyList(list):
    """[Prints a list in sorted order]
    """

    def print_sorted(self):
        """Print list in sorted order
        """
        print(sorted(self))
