#!/usr/bin/python


def none1(a,b):
    if a > b:
        return "a>b"
    else:
        return None                # Explicitly return None

def none2(a,b):
    return                         # no return value means, return None

def none3(a,b):
    pass                           # No return statement means, return None

if __name__ == "__main__":
    print "none1:", none1(5,12)
    print "none2:", none2(5,12)
    print "none3:", none3(5,12)
