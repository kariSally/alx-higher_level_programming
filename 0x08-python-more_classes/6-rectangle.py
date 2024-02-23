#!/usr/bin/python3
"""A module for dealing with a rectangle class."""


class Rectangle:
    """A class that represents a rectangle."""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Construct an instance."""
        Rectangle.number_of_instances += 1
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

    def __str__(self):
        """Convert class to string."""
        if self.width == 0 or self.height == 0:
            return ''
        shape = ''
        for _ in range(self.height):
            for _ in range(self.width):
                shape += '#'
            shape += '\n'
        shape = shape[:-1]
        return shape

    def __repr__(self):
        """Convert class to string representation."""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Delete Class."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
