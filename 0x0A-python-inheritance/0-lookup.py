#!/usr/bin/python3
"""
defines  the function lookup
"""


def lookup(obj):
    """Returns list of attributes and methods of an object
    Args:
        obj: object whose attributes and methods are returned
    """

    return (dir(obj))
