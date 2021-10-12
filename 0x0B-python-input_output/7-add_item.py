#!/usr/bin/python3


"""
Imports the json and sys modules
"""
import json
from sys import argv
"""
Imports modules for custom functions to be used
"""

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


try:

    mylist = load_from_json_file("add_item.json")
    for i in range(1, len(argv)):
        mylist.append(argv[i])
    save_to_json_file(mylist, "add_item.json")

except:

    mylist = []

    for i in range(1, len(argv)):
        mylist.append(argv[i])

    save_to_json_file(mylist, "add_item.json")
