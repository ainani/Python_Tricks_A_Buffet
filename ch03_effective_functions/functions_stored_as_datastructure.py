#!/usr/bin/python


def mul(a,b):
    return a*b


def add(a,b):
    return a+b

def div(a,b):
    return a/b

if __name__ == "__main__":
    operations = [mul, add, div]
    for opr in operations:
        print opr, opr(12,3)

    ### Calling indexed operations
    print operations[0](5,4)
    print operations[1](5,4)
    print operations[2](5,4)
