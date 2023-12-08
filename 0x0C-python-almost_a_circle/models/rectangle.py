#!/usr/bin/python3
""" defines class Rectangle,
inheritance of class Base
"""
from models.base import Base


class Rectangle(Base):
    """ Class Rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializes instances """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        '''width of rect'''
        return self.__width
    
    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        """ height of rect """
        return self.__height
    
    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        '''x of rect'''
        return self.__x
    
    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        '''y of rect'''
        return self.__y
    
    @y.setter
    def y(self, value):
        self.__y = value
