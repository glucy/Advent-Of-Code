'''
Created on 2 Dec 2015

@author: glucy
'''


class DayOne():

    floor = 0
    counter = 0
    firstTimeInBasement = 0

    def __init__(self):
        pass

    def inBasement(self, currentFloor):
        if (currentFloor == -1):
            return True

    def floorsAndBasement(self, value):
        for i in value:
            DayOne.counter += 1

            if (i is "("):
                DayOne.floor += 1
            elif (i is ")"):
                DayOne.floor -= 1
                if (self.inBasement(DayOne.floor)):
                    print "Basement Char Count: ", DayOne.counter
        print "Floor: ", DayOne.floor

with open("/Users/glucy/code/AdventOfCode/resources/adventofcode/dayOne", "r") as f:
    dayOne = DayOne()
    dayOne.floorsAndBasement(f.readline())
