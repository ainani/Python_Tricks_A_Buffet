#!/usr/bin/python

def list_comp():
    return [i*i for i in range(0,10)]
    

def list_comp_with_cond():
    return [i*i for i in range(0,10) if i%2 == 0]

def dict_comp():
    return {i: i*i for i in range(0,10)}

def set_comp():
    return {i*i for i in range(-9,10)}


if __name__ == "__main__":
    print list_comp()
    print list_comp_with_cond()
    print dict_comp()
    print set_comp()
