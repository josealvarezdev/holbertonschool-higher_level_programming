#!/usr/bin/python3
"""
    Square class created
"""


class Square:
    """
        Create a instance size inside square class
    """

    def __init__(self, size=0):
        """ Size init"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return (self.__size * self.__size)
