#!/usr/bin/python

import operator

def dict_sort_keys():
    return sorted(dict1.items())                            # sort the dict based on keys


def dict_sort_values_lambda():
    return sorted(dict1.items(), key=lambda x: x[1])         # sort the dict based on values with lambda

def dict_sort_values_itemgetter():
    return sorted(dict1.items(), key=operator.itemgetter(1))         # sort the dict based on values with operator.itemgetter

def dict_sort_values_lambda_with_abs():
    dict1={'Abhishek':100.5,
            'Rahul':-100.25,
            'Rajat':100.22
            }
    return sorted(dict1.items(), key=lambda x: abs(x[1]))         # sort the dict based on values with operator.itemgetter

def dict_sort_values_lambda_vs_itemgetter():
    dict1={'Abhishek':100.5,
            'Rahul':-100.25,
            'Rajat':100.22
            }
    return sorted(dict1.items(), key=operator.itemgetter(1))         # sort the dict based on values with operator.itemgetter

def dict_sort_values_lambda_with_abs_reverse():
    dict1={'Abhishek':500.5,
            'Rahul':-100.25,
            'Rajat':10.22
            }
    return sorted(dict1.items(), key=lambda x: abs(x[1]), reverse=True)         # sort the dict based on values with operator.itemgetter


if __name__ == "__main__":
    dict1={'Abhishek':500, 
            'Rahul':100,
            'Rajat':200
            }
    print dict_sort_keys()
    print dict_sort_values_lambda()
    print dict_sort_values_itemgetter()
    print dict_sort_values_lambda_with_abs()
    print dict_sort_values_lambda_vs_itemgetter()
    print dict_sort_values_lambda_with_abs_reverse()
