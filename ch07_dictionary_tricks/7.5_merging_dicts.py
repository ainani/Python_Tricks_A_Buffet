#!/usr/bin/python


def update(dict1, dict2):
    for k, v in dict2.items():
        dict1[k] = v

def dict_update(dict1, dict2):
    dict1.update(dict2)

def dict_update_asteriks(dict1, dict2):
    return dict(dict1, **dict2)

if __name__ == "__main__":
    dict1 = {'a':1, 'b':2, 'c':3}
    dict2 = {'d':5, 'c':6, 'f':7}
    update(dict1, dict2)
    print dict1
    dict_update(dict1, dict2)
    print dict1
    print dict_update_asteriks(dict1, dict2)
    
