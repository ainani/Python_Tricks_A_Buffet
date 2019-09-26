#!/usr/bin/python


class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __str__(self):
        return self.color


if __name__ == "__main__":
    myCar = Car('red', 15.9)
    print myCar
    print myCar.color, myCar.mileage

    print "\n", myCar
