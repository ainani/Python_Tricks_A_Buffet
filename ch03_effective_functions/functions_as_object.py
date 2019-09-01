#!/usr/bin/python


def mul(a,b):
    return a*b

if __name__ == "__main__":
    print "mul:", mul(2,5)
    mul1=mul
    print "mul1:", mul1(5,10)
    del mul
    try:
        print "mul:", mul(2,5)
    except NameError as e:
        print e
    print "AFter deleting mul, mul1 :", mul1(100,10)
    print "String Identifier for mul1:", mul1.__name__
