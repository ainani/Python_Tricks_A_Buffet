#!/usr/bin/python


def mul(a,b):
    def pow(a,b):
        return a**b
    return pow(a,b)


def add(a,b):
    return a+b

def div(a,b):
    def floor(a,b):
        return a//b
    if a < b:
        return floor(a,b)
    return a/b

if __name__ == "__main__":
    print "mul:", mul(5,2)
    #print pow(5,2)
    #print mul.pow(5,2)
    print div(5,12)
    print div(5,3)
