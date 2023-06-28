#!/usr/bin/python3
'''create a base class'''


import json
import os


class Base:
    '''create the base class'''

    __nb_objects = 0

    def __init__(self, id=None):
        '''create an id for instances'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''dict to json'''
        if list_dictionaries is None:
            return ("[]")
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''JSON string to file'''
        if list_objs is None:
            list_objs = []

        my_dict = []
        for obj in list_objs:
            my_dict.append(obj.to_dictionary())
        obj = cls.to_json_string(my_dict)
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            f.write(obj)

    @staticmethod
    def from_json_string(json_string):
        '''from JSON to string'''
        my_list = []
        if json_string is None:
            return my_list
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''dictionnary to instance'''
        path = cls
        if cls.__name__ == "Square":
            my_rectangle = path(5)
        else:
            my_rectangle = path(2, 3)
        my_rectangle.update(**dictionary)
        return (my_rectangle)

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = cls.__name__ + ".json"
        if not os.path.exists(filename):
            return []

        with open(filename, "r") as f:
            file_content = f.read()

        instances_dict = cls.from_json_string(file_content)
        instances = [cls.create(**data) for data in instances_dict]

        return instances
