#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    new_list_with_del = []
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    for i in my_list:
        if i != idx:
            new_list_with_del.append(i)
    my_list = new_list_with_del
    return my_list
