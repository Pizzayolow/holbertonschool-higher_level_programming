#!/usr/bin/python3
'''class to JSON'''


def class_to_json(obj):
    # Check if the object is a dictionary, list, string, integer, or boolean
    if isinstance(obj, dict):
        return {key: class_to_json(value) for key, value in obj.items()}
    elif isinstance(obj, list):
        return [class_to_json(item) for item in obj]
    elif isinstance(obj, str) or isinstance(obj, int) or isinstance(obj, bool):
        return obj
    
    # If the object is not a basic data type, convert it to a dictionary
    attributes = {}
    for attr in obj.__dict__:
        value = getattr(obj, attr)
        if isinstance(value, (list, dict, str, int, bool)):
            attributes[attr] = class_to_json(value)
    return attributes
