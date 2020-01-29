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

def arr_bytes(a):
    a_bytes=bytes(a)
    print (a_bytes)
    try:
        del a_bytes[1]
    except TypeError as e:
        print ("ERROR:", e)

def arr_bytearrays(a):
    a_bytearr=bytearray(a)
    print (a_bytearr)
    a_bytearr[1] = 56
    print (a_bytearr)

if __name__ == "__main__":
    a = arr1()
    print (a)
    print (arr1_mutable(a))
    print ("ERROR: " + str(arr_typed(a)))
    arr_bytes(a)
    arr_bytearrays(a)
