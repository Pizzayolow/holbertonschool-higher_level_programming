#!/usr/bin/python3

"""
return name and lastname
"""


def say_my_name(first_name, last_name=""):
    """
    check if the variables passed are string and print the names
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name)is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
