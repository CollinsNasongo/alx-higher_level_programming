#!/usr/bin/python3
"""A class that defines a Square"""


class Square:
    """A square representation"""

    def __init__(self, size):
        """A new Square

        Args:
            size (int): The size of a new Square.
        """
        self.__size = size

    @property
    def size(self):
        """Getting the size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Setting the size of the square"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the area given the size of square"""
        return (self.__size ** 2)
