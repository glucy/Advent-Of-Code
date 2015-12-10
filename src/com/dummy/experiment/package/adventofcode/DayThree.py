'''
Created on 3 Dec 2015

@author: glucy
'''
import logging

# create logger with 'name'
logger = logging.getLogger("DayThree")
logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
fh = logging.FileHandler('adventofcode.log')
fh.setLevel(logging.DEBUG)
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)


class Coordinate():

    x_coord = 0
    y_coord = 0

    def __init__(self, x, y):
        self.x_coord = x
        self.y_coord = y

    def __hash__(self):
        return hash((self.x_coord, self.y_coord))

    def __eq__(self, other):
        return (self.x_coord, self.y_coord) == (other.x_coord, other.y_coord)


class DayThree():

    def __init__(self):
        pass

    def nextHouse(self, arrow, coord):
            if arrow == '>':
                coord.x_coord += 1
            elif arrow == '<':
                coord.x_coord -= 1
            elif arrow == '^':
                coord.y_coord += 1
            elif arrow == 'v':
                coord.y_coord -= 1
            nextCoord = Coordinate(coord.x_coord, coord.y_coord)
            return nextCoord


with open("/Users/glucy/code/AdventOfCode/resources/adventofcode/dayThree", "r") as f:
    dayThree = DayThree()
    houses = set()
    houses.add(Coordinate(0, 0))
    phase1 = Coordinate(0, 0)
    logger.debug(">>> Phase 1 TEST TEST TEST <<<")
    for arrow in f.readline():
        phase1 = dayThree.nextHouse(arrow, phase1)
        houses.add(Coordinate(phase1.x_coord, phase1.y_coord))

print "Number of Houses for Phase 1: ", len(houses)
# Number of Houses for Phase 1:  2592

with open("/Users/glucy/code/AdventOfCode/resources/adventofcode/dayThree", "r") as f:
    dayThree = DayThree()
    houses = set()
    houses.add(Coordinate(0, 0))
    santa = Coordinate(0, 0)
    robot = Coordinate(0, 0)
    count = 1
    logger.debug(">>> Santa & Robot TEST TEST TEST <<<")
    for arrow in f.readline():
        # Santa
        if count % 2 != 0:
            santa = dayThree.nextHouse(arrow, santa)
            houses.add(Coordinate(santa.x_coord, santa.y_coord))
            count += 1
        # Robot
        elif count % 2 == 0:
            robot = dayThree.nextHouse(arrow, robot)
            houses.add(Coordinate(robot.x_coord, robot.y_coord))
            count += 1

print "Number of Houses for Santa & Robot: ", len(houses)
# Number of Houses for Santa & Robot:  2360
