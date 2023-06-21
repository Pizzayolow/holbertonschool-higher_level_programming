#!/usr/bin/python3
'''append to a file'''


def write_file(filename="", text=""):
    '''append to a file'''
    if filename == None:
        f = open(filename, "x", encoding='utf-8')
    with open(filename, "w", encoding='utf-8') as f:
        return f.write(text)
