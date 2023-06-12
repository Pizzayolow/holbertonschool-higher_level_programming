#!/usr/bin/python3
"""first file with a classe of a square in Python"""


class Square:
    """class of a square, size given and checkore than zero"""
    def __init__(self, size=0):
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self._Square__size = size
        else:
            raise TypeError("size must be an integer")
