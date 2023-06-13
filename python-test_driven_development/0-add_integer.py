#!/usr/bin/python3
"""
function


"""


def add_integer(a, b=98):
    """
    add two integers and return the sum
    """
    try:
        if not isinstance(a, (int, float)):
            raise TypeError("a must be an integer")
        if not isinstance(b, (int, float)):
            raise TypeError("b must be an integer")
        sum = int(a) + int(b)
        if sum == float('inf') or sum == -float('inf'):
            return 89
        return sum
    except Exception as e:
        return e
