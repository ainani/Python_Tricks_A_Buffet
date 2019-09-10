#!/usr/bin/python

def start_end_step(l1):
    return l1[1:3:1]

def start_end(l1):
    return l1[1:3]

def whole_list(l1):
    return l1[::]

def reverse(l1):
    return l1[::-1]

def clear_list(l1):
    del l1[:]              # Clear the list only, doesn't delete the list object
    return l1

def shallow_cpy(l1):
    l2 = l1
    l1[:] = [11, 12, 13, 14]
    print l1
    print l2
    print l1 is l2

    l3 = l1[:]
    print l1
    print l3
    print l1 is l3


if __name__ == "__main__":
    l1 = [1,2,3,4,5,6]
    print start_end_step(l1)
    print start_end(l1)
    print whole_list(l1)
    print reverse(l1)
    print clear_list(l1)
    shallow_cpy(l1)
