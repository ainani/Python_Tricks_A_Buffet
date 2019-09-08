#!/usr/bin/python


def bool_as_idx(list1):
    print list1
    print list1[True]
    print list1[False]
    print list1[True + False]
    print list1[True + True]

def keys_will_not_change(dict1):
    dict1[1.0] = 7
    dict1[1] = 7
    print dict1

class AlwaysEquals:
    def __eq__(self, other):
        return True

    def __hash__(self):
        return id(self)

class SameHash:
    def __hash__(self):
        return 1                             # Always return hash id as 1

if __name__ == "__main__":
    dict1 = {True: 'yes', 1: 'no', 1.0: 'maybe'}
    print dict1        # True == 1.0 == 1 (so here all keys of a dictionary are equal)
    """ Explanation:  As far as Python is concerned, True, 1, and 1.0 all represent the same
                      dictionary key. As the interpreter evaluates the dictionary expression,
                      it repeatedly overwrites the value for the key True. This explains why,
                      in the end, the resulting dictionary only contains a single key.
    """
    list1=['a', 2, 3]
    bool_as_idx(list1)
    keys_will_not_change(dict1)             # since all keys are same so dict will not modify the keys object by itself


    print AlwaysEquals() == AlwaysEquals()
    print AlwaysEquals() == 7
    print AlwaysEquals() == 'a'
    objects = [AlwaysEquals(), AlwaysEquals(), AlwaysEquals()]
    print [hash(obj) for obj in objects]
    print {AlwaysEquals(): 'yes', AlwaysEquals(): 'no'}

    a = SameHash()                 
    b = SameHash()

    print ('\na=' + str(a) + '\nb=' + str(b) + '  and\na == b is ' + str(a == b))                           # Since a != b it will return as false
    print (hash(a), hash(b))                                                                                # but there has values are equal

    print (hash(True), hash(1), hash(1.0))                      # Hash value of all 3 is equal
