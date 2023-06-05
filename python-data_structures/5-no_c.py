#!/usr/bin/env python3
def no_c(my_string):
    cp_string = ""
    for i in my_string:
        if ord(i) != 99 and ord(i) != 67:
            cp_string += i
    return cp_string
