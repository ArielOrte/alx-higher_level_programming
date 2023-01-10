#!/usr/bin/python3
"""

Module with save_to_json_file.

"""

import json


def save_to_json_file(my_obj, filename):
    """Function that writes an Object to a text file,
    using JSON representation."""

    with open(filename, 'w') as f:
        filename = f.write(json.dumps(my_obj))
    return filename
