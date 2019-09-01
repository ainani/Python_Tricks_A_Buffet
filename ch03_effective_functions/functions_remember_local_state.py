#!/usr/bin/python


def mul(a,b):
    def pow():
        return a**b
    return pow()


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
