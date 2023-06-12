#!/usr/bin/python3
"""first file with a classe of a square in Python"""


class Square:
    """class of a square, size given and checkore than zero"""
    def __init__(self, size=0):
        self.size = size

    def area(self):
        return (self._Square__size * self._Square__size)

    @property
    def size(self):
        return self._Square__size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self._Square__size = value
        else:
            raise TypeError("size must be an integer")
