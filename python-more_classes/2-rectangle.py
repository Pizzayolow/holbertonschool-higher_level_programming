#!/usr/bin/python3
"""
print a rectangle
"""


class Rectangle:
    """rectangle"""

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def width(self):
        return self._Rectangle__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self._Rectangle__width = value

    @property
    def height(self):
        return self._Rectangle__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self._Rectangle__height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        perimeter = 0
        if self.width == 0 or self.height == 0:
            perimeter = 0
        perimeter = (self.width + self.height) * 2
        return perimeter
