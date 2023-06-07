#!/usr/bin/python3
def safe_print_division(a, b):
    sum = 0
    try:
        sum = a / b
    except ZeroDivisionError:
        return
    finally:
        print("Inside result: {}".format(sum))
        return sum
