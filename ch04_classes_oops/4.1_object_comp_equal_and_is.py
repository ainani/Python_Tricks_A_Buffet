#!/usr/bin/python

def equality(a, b):
   return a == b

def identity(a, b):
    return a is b


if __name__ == "__main__":
    a = [1, 2, 3]
    b = a
    print "a:", a
    print "b:", b

    print "Equality:", equality(a, b)
    print "Identity:", identity(a, b)

    c = list(a)
    print "\nEquality:", equality(a, c)
    print "Identity:", identity(a, c)
