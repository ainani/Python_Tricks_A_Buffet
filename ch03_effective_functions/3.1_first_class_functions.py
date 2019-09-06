#!/usr/bin/python

def mul(a,b):
    return a*b

def add(a,b):
    return a+b

def div(a,b):
    return a/b


if __name__ == "__main__":
    print " - Functions stored as data structures"
    operations = [mul, add, div]
    for opr in operations:
        print opr, opr(12,3)

    ### Calling indexed operations
    print operations[0](5,4)
    print operations[1](5,4)
    print operations[2](5,4)
    print "mul:", mul(2,5)
    
    print "\n\n Functions calling other function"
    print mul(add(div(3,2), 4), 2)
    
    print "\n\n - Functions as an objects"
    mul1=mul
    print "mul1:", mul1(5,10)
    del mul
    try:
        print "mul:", mul(2,5)
    except NameError as e:
        print e
    print "After deleting mul, mul1 :", mul1(100,10)
    print "String Identifier for mul1:", mul1.__name__

