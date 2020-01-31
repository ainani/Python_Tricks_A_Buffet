#!/usr/bin/python
iterator = ('Hello' for i in range(3))

print list(iterator)       

# OR                       # only one of these 2 methods can be used at a time 

for i in iterator:
    print i                # This will print nothing because once generator object is consumed it can't be reused again


print ("\nConditional Generator expression")
### Conditional Generator expression
iter_cond = (x*x for x in range(10) if x%2 == 0)
for i in iter_cond:
    print i



print ("\nGenerator expression as in-line generator expr for iterators (for-in loop)")
### Generator expression as in-line generator expr for iterators (for-in loop)
for i in (x*x for x in range(10) if x%2 == 0):
    print i
