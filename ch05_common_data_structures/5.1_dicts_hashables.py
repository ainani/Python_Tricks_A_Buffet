#!/usr/bin/python

import collections

def nrml_dict(dict1):
    return dict1

def ordrd_dict(dict1):
    return collections.OrderedDict(dict1)

def dflt_dict(dict1):
    dict1 = collections.defaultdict(int)
    #print dict1['four']
    return dict1['four']

def dict_chain():
    dict1 = {'one': 1, 'two': 2}
    dict2 = {'three': 3, 'four': 4}
    chain = collections.ChainMap(dict1, dict2)
    return chain

if __name__ == "__main__":
    dict1 = {'one': 1, 'two': 2, 'three': 3}
    print nrml_dict(dict1)
    print ordrd_dict(dict1)      # As nrml_dict will return the arbitrary order same order will be used for ordrd_dict function
    print dflt_dict(dict1)
    print dict_chain()

