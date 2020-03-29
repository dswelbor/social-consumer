"""
This module implements utility function(s) such as translating python 
objects into dictionaries for the purpose of json serialization.
"""

import json

def to_dict(obj_list):
    """
    Utility method accepts a passed list of objects and returns a list 
    of dictionaries.
    """
    # Convert list of objects to list of dictionaries
    new_list = []
    for obj in obj_list:
        new_list.append(obj.__dict__)
        
    return new_list

