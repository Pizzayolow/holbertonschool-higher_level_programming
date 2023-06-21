#!/usr/bin/python3
'''to json to string'''


import json


def save_to_json_file(my_obj, filename):
    '''save oject to a file'''
    with open(filename, "w", encoding='utf-8') as f:
        json.dump(my_obj, f)
