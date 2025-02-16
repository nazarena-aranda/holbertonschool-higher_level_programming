#!/usr/bin/python3
"""
module with function
"""
import sys
import json


def save_to_json_file(my_obj, filename):
    """
    function that writes an Object to a text file, using a JSON representation
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)


def load_from_json_file(filename):
    """
    Write a function that creates an Object from a “JSON file”:
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)


def add_items():
    """
    script that adds all arguments to a Python list,
    and then save them to a file
    """
    filename = "add_item.json"
    try:
        items = load_from_json_file(filename)
    except FileNotFoundError:
        items = []

    items.extend(sys.argv[1:])
    save_to_json_file(items, filename)
