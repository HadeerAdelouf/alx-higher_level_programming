#!/usr/bin/paython3
"""module for say my name function"""


def say_my_name(first_name, last_name=""):
    """ Method for printing first and last name

    args:
        @first_name : string with first name
        @last_name : string of last_name

    Raises:
        TypeError : if first_name or last_name not a string
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
