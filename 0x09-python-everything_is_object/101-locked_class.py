#!/usr/bin/python3
"""Defines LockedClass class """


class LockedClass():
    """ all attrs locked except first_name atrr """
    __slots__ = ('first_name')
