#!/usr/bin/python
def repeater(value, max_repeats):
    for i in range(max_repeats):
        yield value
        
for item in repeater("hello", 3):
    print(item)



