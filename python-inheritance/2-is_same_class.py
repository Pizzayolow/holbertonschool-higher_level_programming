#!/usr/bin/python3
'''check if is isinstance'''


def is_same_class(obj, a_class):
    '''check if obj == aclass'''
    if type(obj) == a_class:
        return True
    return False
