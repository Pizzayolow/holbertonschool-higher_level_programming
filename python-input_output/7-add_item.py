#!/usr/bin/python3


import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
my_list = []
for args in range(1, len(sys.argv)):
    my_list.append(sys.argv[args])
print(my_list)
save_to_json_file(my_list, filename)
