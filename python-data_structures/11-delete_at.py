#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    new_list_with_del = []
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    for i in my_list:
        if i != idx + 1:
            new_list_with_del.append(i)
    my_list.clear()
    for i in new_list_with_del:
        my_list.append(i)
    return my_list
