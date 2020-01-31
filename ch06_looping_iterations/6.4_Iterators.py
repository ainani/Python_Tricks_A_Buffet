#!/usr/bin/python
class Repeater:
    def __init__(self, value, max_repeats):
        self.value = value
        self.max_repeats = max_repeats
        self.count = 0

    def __iter__(self):
        return self

    # For Python 3
    def __next__(self):
        if self.count >= self.max_repeats:
            raise StopIteration
        self.count += 1
        return self.value
    

    # For Python 2
    def next(self):
        print self.count
        if self.count >= self.max_repeats:
            raise StopIteration
        self.count += 1
        return self.__next__()

repeater = Repeater('Hello', 3)
for item in repeater:
    print(item)


