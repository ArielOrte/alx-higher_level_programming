#!/usr/bin/python3
"""

Module with from_json_string.

"""

import json


def from_json_string(my_str):
    """Function that returns he JSON representation of an object(string)."""

    return json.loads(my_str)
