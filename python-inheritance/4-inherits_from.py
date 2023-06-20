#!/usr/bin/python3
'''same class or inherit from'''


def inherits_from(obj, a_class):
    '''only sub class of'''
    if type(obj) != a_class and issubclass(type(obj), a_class):
        return True
    return False
