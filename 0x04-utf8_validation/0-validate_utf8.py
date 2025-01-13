#!/usr/bin/python3
"""
module: 0-validate_utf8
description: validate if data is utf-8 encoded.
"""


def validUTF8(data):
    """@description.
    Args:
        data (list): input data.
    Returns:
        boolean value.
    """
    number_bytes = 0
    mask_one = 1 << 7
    mask_two = 1 << 6

    for i in data:
        mask_byte = 1 << 7
        if number_bytes == 0:
            while mask_byte & i:
                number_bytes = number_bytes + 1
                mask_byte = mask_byte >> 1

            if number_bytes == 0:
                continue
            if number_bytes == 1 or number_bytes > 4:
                return False
        else:
            if not (i & mask_one and not (i & mask_two)):
                return False
        number_bytes -= 1
    if number_bytes == 0:
        return True
    return False
