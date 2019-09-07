#!/usr/bin/python

def dict_default(key):
    dict1={'Abhishek':50, 
            'Rahul':100,
            'Rajat':200
            }
    return 'Hi %s, You won %d INR !' % (key, dict1.get(key, 0))


if __name__ == "__main__":
    print dict_default('Abhishek')
    print dict_default('Rahul')
    print dict_default('Paras')
