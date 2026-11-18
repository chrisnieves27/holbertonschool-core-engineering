#!/usr/bin/python3
"""Define a square with size, position, and string representation."""


class Square:
    """Represent a square with a validated size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square size and position."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Return the square size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size to a non-negative integer."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Return the square position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position to a tuple of two non-negative integers."""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(item, int) and item >= 0
                        for item in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the square area."""
        return self.__size ** 2

    def my_print(self):
        """Print the square using its string representation."""
        print(str(self))

    def __str__(self):
        """Return the square drawn with hashes at its position."""
        if self.__size == 0:
            return ""
        row = " " * self.__position[0] + "#" * self.__size
        return "\n" * self.__position[1] + "\n".join(
            row for _ in range(self.__size))
