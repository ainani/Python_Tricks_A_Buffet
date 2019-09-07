#!/usr/bin/python

import operator

def ifElse(string):
    if string == 'a':
        return 'A'
    elif string == 'b':
        return 'B'
    elif string == 'c':
        return 'C'
    else:
        return

def dict_switch(number):
    dict1={'a':'A',
            'b':'B',
            'c':'C',
            }
    return dict1.get(number, None)


if __name__ == "__main__":
    print ifElse('a')
    print ifElse('b')
    print ifElse('c')
    print ifElse('d')
    print dict_switch('a')
    print dict_switch('b')
    print dict_switch('c')
    print dict_switch('d')
