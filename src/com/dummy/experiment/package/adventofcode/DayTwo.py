'''
Created on 2 Dec 2015

@author: glucy
'''


class DayTwo():

    def __init__(self):
        pass

    def calculateAreaOfSmallestSide(self, l, w, h):
        smallestSide = 0
        if (l*w < smallestSide or smallestSide == 0):
            smallestSide = l*w
        if (w*h < smallestSide):
            smallestSide = w*h
        if (h*l < smallestSide):
            smallestSide = h*l
        print "SmallestSide: ", smallestSide
        return smallestSide

    def calculateBox(self, sides):
        print "Rectangle Dimensions: ", sides
        totalArea = 0
        l = int(sides[0])
        print "length: ", l
        w = int(sides[1])
        print "width: ", w
        h = int(sides[2])
        print "height: ", h
        # 2*l*w + 2*w*h + 2*h*l
        totalArea += 2*l*w + 2*w*h + 2*h*l
        print "Area: ", totalArea
        totalArea += self.calculateAreaOfSmallestSide(l, w, h)
        print "Area + Extra", totalArea
        return totalArea

    def calculateBow(self, l, w, h):
        length = l * w * h
        print "Bow: ", length
        return length

    def calculateRibbon(self, sides):
        totalLength = 0
        print sides
        l = sides[0]
        w = sides[1]
        h = sides[2]
        totalLength += l + l + w + w
        print "Parameter: ", totalLength
        totalLength += self.calculateBow(l, w, h)
        print "Ribbon: ", totalLength
        return totalLength


with open("/Users/glucy/code/AdventOfCode/resources/adventofcode/dayTwo", "r") as f:
    dayTwo = DayTwo()
    totalarea = 0
    totalribbon = 0
    listOfLines = f.readlines()
    for line in listOfLines:
        sides = line.split('x')
        sides = map(int, sides)
        sides.sort()
        totalarea += dayTwo.calculateBox(sides)
        totalribbon += dayTwo.calculateRibbon(sides)

    print "Total Area: ", totalarea
    print "Total Ribbon: ", totalribbon
    # Total Area:  1586300
    # Total Ribbon:  3737498
