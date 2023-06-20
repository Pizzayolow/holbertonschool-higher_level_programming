#!/usr/bin/python3
'''rectangle'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''rectangle'''
    def __init__(self, width, height):
        self.__width = BaseGeometry.integer_validator(self, '', width)
        self.__height = BaseGeometry.integer_validator(self, '', height)
