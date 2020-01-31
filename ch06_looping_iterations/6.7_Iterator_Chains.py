#!/usr/bin/python
iterator = range(10)
squared = (i*i for i in iterator)
negated = (-i for i in squared)

print list(negated)       
