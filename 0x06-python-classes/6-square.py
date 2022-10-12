#!/usr/bin/python3
"""A class that defines a Square
    Private instance attribute: size:
        - property def size(self)
        - property setter def (self, value)
    Instantiation with optional size.
    Public instance method: def area(self).
    Public instance method: def my_print(self).
    Instantiation with optional size and optional position.
    Public instance method: def area(self).
    Public instance method: def my_print(self).
"""


class Square:
    """A square representation"""

    def __init__(self, size=0, position=(0, 0)):
        """A new Square

        Args:
            size (int): The size of a new Square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getting the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setting the size of the value"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getting the position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setting the position value"""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """Return the area given the size of square"""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with character '#'"""
        if self.__size == 0:
            print()
        else:
            for i in range(0, self.__size):
                for j in range(0, self.__size):
                    print("#", end='')
                print()
