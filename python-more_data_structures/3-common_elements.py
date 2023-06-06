#!/usr/bin/python3
def common_elements(set_1, set_2):
    my_list = []
    for element in set_1:
        for element2 in set_2:
            if element == element2:
                my_list.append(element)
    return my_list