#!/usr/bin/python3
"""
function creates an object from json file
"""

import json

def load_from_json_file(filename):
    """creat an object from json file"""
    with open(filename, 'r', encoding='utf_8') as f:
        return json.load(f)
