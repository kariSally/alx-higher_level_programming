#!/usr/bin/python3
"""A class Square that defines a square."""


class Square:
    """A Square class."""

    def __init__(self, size=0, position=(0, 0)):
        """Construct the class."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get size of square."""
        return self.__size

    @property
    def position(self):
        """Get position of square."""
        return self.__position

    @size.setter
    def size(self, value):
        """Set the value of size."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        """Set position of square."""
        if (not isinstance(value, tuple) or len(value) != 2
                or not all((isinstance(i, int) and i >= 0) for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Compute area of square."""
        return self.size ** 2

    def my_print(self):
        """Print in stdout the square."""
        if self.size == 0:
            print()
            return

        for _ in range(self.position[1]):
            print()
        for _ in range(self.size):
            for _ in range(self.position[0]):
                print(' ', end='')
            for _ in range(self.size):
                print("#", end='')
            print()
