#!/usr/bin/python3
'''geometry'''


class BaseGeometry:
    '''geometry'''
    pass

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''check if value is an int and greater than 0'''
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
