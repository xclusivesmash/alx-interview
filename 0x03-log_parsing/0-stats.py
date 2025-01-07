#!/usr/bin/python3
"""
module: 0-stats
description: log parsing problem.
"""
import sys


total_file_size = 0
code = 0
counter = 0
dict_sc = {"200": 0,
           "301": 0,
           "400": 0,
           "401": 0,
           "403": 0,
           "404": 0,
           "405": 0,
           "500": 0}

def print_msg(dict_sc, total_file_size):
    """@description.
    Args:
        dict_sc (dict): dict of status codes
        total_file_size (int): total of the file
    Returns:
        Nothing
    """
    print("File size: {}".format(total_file_size))
    for key, value in sorted(dict_sc.items()):
        if value != 0:
            print("{}: {}".format(key, value))

try:
    for line in sys.stdin:
        parsed_line = line.split()
        parsed_line = parsed_line[::-1]
        if len(parsed_line) > 2:
            counter = counter + 1
            if counter <= 10:
                # file size
                total_file_size += int(parsed_line[0])
                # status code
                code = parsed_line[1]
                if (code in dict_sc.keys()):
                    dict_sc[code] += 1
            if (counter == 10):
                print_msg(dict_sc, total_file_size)
                counter = 0
except Exception:
    pass
finally:
    print_msg(dict_sc, total_file_size)
