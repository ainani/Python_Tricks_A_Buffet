#!/usr/bin/python

import sys
import dis

def format_1_single(name):
    return 'Hi, %s !' %name

def format_1_multi(name, city):
    return 'Hi, %s, Do you stay in %s ?' %(name, city)

def format_1_samePlace(name, city):
    return 'Hi, %(name)s, Do you stay in %(city)s ?' %{'name': name, 'city': city}



def format_2_single(name):
    return 'Hi, {} !'.format(name)

def format_2_multi(name, city):
    return 'Hi, {}, Do you stay in {} ?'.format(name, city)

def format_2_samePlace(name, city):
    return 'Hi, {name}, Do you stay in {city} ?'.format(name=name, city=city)



def format_3_single(name):
    return f'Hi, {name} !'

def format_3_multi(name, city):
    return f'Hi, {name}, Do you stay in {city} ?'

def format_3_arithmetics(a, b):
    return f'Sum of {a} and {b} is, {a + b}'



if __name__ == "__main__":
    version = float(str(sys.version_info[0]) + '.' + str(sys.version_info[1]))
    print ("<---- Old style string formatting ---->")
    print (format_1_single('Abhishek'))
    print (format_1_multi('Abhishek', 'Bangalore'))
    print (format_1_samePlace('Abhishek', 'Bangalore'))
   
    print ("\n <---- New style string formatting ---->")
    print (format_2_single('Abhishek'))
    print (format_2_multi('Abhishek', 'Bangalore'))
    print (format_2_samePlace('Abhishek', 'Bangalore'))
   
    if version >= 3.6:
        print ("\n <---- Literal style string formatting ---->")
        print (format_3_single('Abhishek'))
        print (format_3_multi('Abhishek', 'Bangalore'))
        print (format_3_arithmetics(3, 5))
        print (dis.dis(format_3_arithmetics))
