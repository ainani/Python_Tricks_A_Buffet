#!/usr/bin/python

def print_list(list1):
    for l in list1:
        print (l)

def idx_list(list1):
    print ("\n")
    for i, l in enumerate(list1):
        print (f'{i} : {l}')

def dict_print(dict1):
    print ("\n")
    for k, v in dict1.items():
        print (f'{k} -> {v}')

if __name__ == "__main__":
    list1 = ['a', 1, 'b', 2, 'c']
    print_list(list1)
    idx_list(list1)

    dict1={'fname': 'Abhishek',
            'lname': 'Inani'}
    dict_print(dict1)
