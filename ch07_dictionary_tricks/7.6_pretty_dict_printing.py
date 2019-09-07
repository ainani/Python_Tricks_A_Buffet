#!/usr/bin/python

import json
import pprint

def json_reader(dict1):
    return json.dumps(dict1, indent=4, sort_keys=True)

def pprint(dict1):
    print pprint.PrettyPrinter(dict1)

if __name__ == "__main__":
    dict1 = {'a': 1, 'b' : 'Abhishek Inani', 'c': 0xc0ffe}
    print json_reader(dict1)
    pprint(dict1)
