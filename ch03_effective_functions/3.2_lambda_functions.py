#!/usr/bin/python


if __name__ == "__main__":
    print "Using function definition"
    add = lambda x, y: x + y
    print add (5, 3)

    print "\nWithout using function definition"
    print (lambda x, y : x + y)(5, 3)
