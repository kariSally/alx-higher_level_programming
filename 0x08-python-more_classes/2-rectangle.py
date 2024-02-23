#!/usr/bin/python3
"""A module for dealing with a rectangle class."""


class Rectangle:
    """A class that represents a rectangle."""

    def __init__(self, width=0, height=0):
        """Construct an instance."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get width."""
        return self.__width

    @property
    def height(self):
        """Get height."""
        return self.__height

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Compute Area."""
        return self.width * self.height

    def perimeter(self):
        """Compute Perimeter."""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)
