#!/usr/bin/python3
"""A class Square that defines a square."""


class Square:
    """A Square class."""

    def __init__(self, size=0):
        """Construct the class."""
        self.size = size

    @property
    def size(self):
        """Get size of square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the value of size."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Compute area of square."""
        return self.__size ** 2
