#!/usr/bin/python3
"""

Module with load_from_json_file.

"""

import json


def load_from_json_file(filename):
    """Function that creates an Object from JSON file."""

    with open(filename) as f:
        return json.loads(f.read())
