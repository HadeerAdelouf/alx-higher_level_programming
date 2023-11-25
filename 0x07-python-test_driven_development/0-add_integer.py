#!/usr/bin/python3
"""module for add intger function method"""

def add_integer(a, b=98):
    """ adds intgers
    args:
    @a :first intger
    @b : 98 if not given, second intger
    """
    if type(a) not in (int, float):
        raise TypeError ('a must be an integer')
    if type(b) not in (int, float):
        raise TypeError ('b must be an integer')

    return int(a) + int(b)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
