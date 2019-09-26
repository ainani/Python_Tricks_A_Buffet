#!/usr/bin/python


class PrefixPostfixTest:
    def __init__(self):
        self.__bam__ = 42

def single_underscores():
    for _ in range(5):
        print "Hi, Abhishek !"
    
    #Unpacking expressions as 'don't care' variable to ignore particualr values 
    car = ('red', 12, 'auto', 14.5)
    color, _, _, mileage = car
    print color, _, mileage


    _ = list()          # Defines an empty list without any name
    print _             # Prints empty list
    _.append(1)
    _.append(2)
    _.append(3)
    _.append(4)
    _.append(5)

    print _
     

if __name__ == "__main__":
    double_underscore = PrefixPostfixTest()
    print double_underscore.__bam__

    single_underscores()
