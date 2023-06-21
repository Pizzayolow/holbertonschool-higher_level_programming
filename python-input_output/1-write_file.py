#!/usr/bin/python3
'''append to a file'''


def write_file(filename="", text=""):
    '''append to a file'''
    with open(filename, "w", encoding='utf-8') as f:
        return f.write(text)
