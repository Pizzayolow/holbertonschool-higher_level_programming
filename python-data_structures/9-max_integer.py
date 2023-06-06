#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list.count() == 0:
        return
    maxvalue = my_list[0]
    for i in my_list:
        if maxvalue < i:
            maxvalue = i
    return maxvalue
