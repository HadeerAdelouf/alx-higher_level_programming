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
        """ width setter """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ height of rect """
        return self.__height
    
    @height.setter
    def height(self, value):
        """ height setter """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        '''x of rect'''
        return self.__x
    
    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        '''y of rect'''
        return self.__y
    
    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ returns the area of the rectangle object """
        return self.width * self.height
    
    def display(self):
        """ displays a rectangle """
        rect = self.y * "\n"
        for i in range(self.height):
            rect += (" " * self.x)
            rect += ("#" * self.width) + "\n"

        print(rect, end='')

    def __str__(self):
        """Return the str representation of the Rect"""
        return "[Rectangle] ({}) {}/{} - {}/{}".\
            format(self.id,self.x, self.y,self.width, self.height)
