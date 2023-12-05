#!/usr/bin/python3
"""
Contains definiton for the class MyList that inherits from list.
"""


class MyList(list):
    """definiton for the class MyList that inherits from list.
    """
    def print_sorted(self):
        """Prints list elements in ascending order"""

        print(sorted(self))
