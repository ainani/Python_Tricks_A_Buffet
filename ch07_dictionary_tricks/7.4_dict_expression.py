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

    print [hash(AlwaysEquals), hash(AlwaysEquals), hash(AlwaysEquals)]
