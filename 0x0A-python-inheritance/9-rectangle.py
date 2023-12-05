#!/usr/bin/python3

"""Defines a class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """Intialize a new Rectangle.
        Args:
            width: The width of the new Rectangle.
            height: The height of the new Rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns are of the rectangle"""

        area = self.__width * self.__height
        return area

    def __str__(self):
        """
        Returns string representation of an instance of class rectangle
        """
        return "[{}] {}/{}".format(type(self).__name__,
                                   self.__width, self.__height)
