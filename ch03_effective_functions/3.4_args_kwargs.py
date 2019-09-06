#!/usr/bin/python

def test(arg, *args, **kwargs):
    print arg
    if args:
        print args
    if kwargs:
        print kwargs

if __name__ == "__main__":
    test('Hello !', 1, 2, key1='val1', key2='val2')
