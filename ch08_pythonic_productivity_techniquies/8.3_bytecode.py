#!/usr/bin/python

import dis

def name(name):
    return "Hello, " + name + "!"

if __name__ == "__main__":
    print name('Abhishek')
    print name.__code__.co_code
    print name.__code__.co_consts
    print name.__code__.co_varnames
    print dis.dis(name)
