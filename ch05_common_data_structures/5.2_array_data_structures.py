#!/usr/bin/python

import array

def arr1():
    a = array.array('f', (1, 2, 3,4 ))
    return a


def arr1_mutable(a):
    a[1] = 7
    return a


def arr_typed(a):
    try:
        a[1]='hi'
        return a
    except TypeError as e:
        return e

if __name__ == "__main__":
    a = arr1()
    print a
    print arr1_mutable(a)
    print "ERROR: " + str(arr_typed(a))
