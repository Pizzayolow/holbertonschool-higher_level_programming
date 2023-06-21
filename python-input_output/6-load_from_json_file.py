#!/usr/bin/python3
'''create object from json file'''


import json


def load_from_json_file(filename):
    '''create object from json file'''
    with open(filename, "r", encoding='utf-8') as f:
        data = json.load(f)
    return data
