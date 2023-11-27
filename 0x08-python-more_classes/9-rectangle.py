#!/usr/bin/python3

"""defines a Rectangle class."""


class Rectangle:
    """Represent an empty Rectangle class.
        Attrs:
        number_of_instances: The number of Rectangle instances
        print_symbol:symbol used for string representation"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.
        Args:
            width: The width of the Rectangle.
            height: The height of the Rectangle.
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """Get the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def perimeter(self):
        """get perimeter of rect"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (2 * (self.height + self.__width))

    def area(self):
        """get area of rect"""
        return (self.__height * self.__width)

    def __str__(self):
        """returns readable presentaion of
        width and height by # sign"""
        if self.__width == 0 or self.__height == 0:
            return ("")

        RectangLe = []
        for i in range(self.__height):
            [RectangLe.append(str(self.print_symbol))
             for j in range(self.__width)]
            if i != self.__height - 1:
                RectangLe.append("\n")
        return ("".join(RectangLe))

    def __repr__(self):
        """return str representaion of rectangle
        for developers"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Print a message for every deletion of a Rectangle."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the Rectangle with the bigger area
        Args:
            rect_1: The first Rectangle.
            rect_2: The second Rectangle.
        Raises:
            TypeError: If either of rect_1 or rect_2 is not a Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    @classmethod
    def square(cls, size=0):
        """Return a new Rect with width and height equal to size.
        Args:
            size:The width and height of the new Rectangle.
        """
        return (cls(size, size))
