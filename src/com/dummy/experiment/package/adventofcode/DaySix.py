'''
Created on 6 Dec 2015

@author: glucy
'''


class DaySix():

    def __init__(self):
        pass

    def turnOn(self, coord1, coord2, grid):
        for x in range(coord1.x, coord2.x + 1):
            for y in range(coord1.y, coord2.y + 1):
                grid[x][y] = True
        return grid

    def turnOff(self, coord1, coord2, grid):
        for x in range(coord1.x, coord2.x + 1):
            for y in range(coord1.y, coord2.y + 1):
                grid[x][y] = False
        return grid

    def toggle(self, coord1, coord2, grid):
        for x in range(coord1.x, coord2.x + 1):
            for y in range(coord1.y, coord2.y + 1):
                if grid[x][y] == False:
                    grid[x][y] = True
                elif grid[x][y] == True:
                    grid[x][y] = False
        return grid

    def turnOnPart2(self, coord1, coord2, grid):
        for x in range(coord1.x, coord2.x + 1):
            for y in range(coord1.y, coord2.y + 1):
                grid[x][y] += 1
        return grid

    def turnOffPart2(self, coord1, coord2, grid):
        for x in range(coord1.x, coord2.x + 1):
            for y in range(coord1.y, coord2.y + 1):
                if grid[x][y] > 0:
                    grid[x][y] -= 1
        return grid

    def togglePart2(self, coord1, coord2, grid):
        for x in range(coord1.x, coord2.x + 1):
            for y in range(coord1.y, coord2.y + 1):
                grid[x][y] += 2
        return grid

    def parseInstructions(self, instruction, grid):
        if "turn on" in instruction:
            a = instruction[8:instruction.index("through") - 1]
            b = instruction[instruction.index("through") + 8:len(instruction)]
            listA = a.split(',')
            listB = b.split(',')
            coord1 = Coord(int(listA[0]), int(listA[1]))
            coord2 = Coord(int(listB[0]), int(listB[1]))
            return self.turnOn(coord1, coord2, grid)

        elif "turn off" in instruction:
            a = instruction[9:instruction.index("through") - 1]
            b = instruction[instruction.index("through") + 8:len(instruction)]
            listA = a.split(',')
            listB = b.split(',')
            coord1 = Coord(int(listA[0]), int(listA[1]))
            coord2 = Coord(int(listB[0]), int(listB[1]))
            return self.turnOff(coord1, coord2, grid)

        elif "toggle" in instruction:
            a = instruction[7:instruction.index("through") - 1]
            b = instruction[instruction.index("through") + 8:len(instruction)]
            listA = a.split(',')
            listB = b.split(',')
            coord1 = Coord(int(listA[0]), int(listA[1]))
            coord2 = Coord(int(listB[0]), int(listB[1]))
            return self.toggle(coord1, coord2, grid)

    def parseInstructionsPart2(self, instruction, grid):
        if "turn on" in instruction:
            a = instruction[8:instruction.index("through") - 1]
            b = instruction[instruction.index("through") + 8:len(instruction)]
            listA = a.split(',')
            listB = b.split(',')
            coord1 = Coord(int(listA[0]), int(listA[1]))
            coord2 = Coord(int(listB[0]), int(listB[1]))
            return self.turnOnPart2(coord1, coord2, grid)

        elif "turn off" in instruction:
            a = instruction[9:instruction.index("through") - 1]
            b = instruction[instruction.index("through") + 8:len(instruction)]
            listA = a.split(',')
            listB = b.split(',')
            coord1 = Coord(int(listA[0]), int(listA[1]))
            coord2 = Coord(int(listB[0]), int(listB[1]))
            return self.turnOffPart2(coord1, coord2, grid)

        elif "toggle" in instruction:
            a = instruction[7:instruction.index("through") - 1]
            b = instruction[instruction.index("through") + 8:len(instruction)]
            listA = a.split(',')
            listB = b.split(',')
            coord1 = Coord(int(listA[0]), int(listA[1]))
            coord2 = Coord(int(listB[0]), int(listB[1]))
            return self.togglePart2(coord1, coord2, grid)

    def numOfLightsOn(self, grid):
        count = 0
        for x in range(1000):
            for y in range(1000):
                if grid[x][y] == True:
                    count += 1
        return count

    def totalBrightness(self, grid):
        count = 0
        for x in range(1000):
            for y in range(1000):
                    count += grid[x][y]
        return count


class Coord():

    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

with open("/Users/glucy/code/AdventOfCode/resources/adventofcode/daySix", "r") as f:
    lines = f.readlines()
    grid = [[0 for x in range(1000)] for x in range(1000)]
    for x in range(1000):
        for y in range(1000):
            grid[x][y] = False
    daySix = DaySix()
    for line in lines:
        grid = daySix.parseInstructions(line, grid)
    print "Number of lights on: ", daySix.numOfLightsOn(grid)
#     Number of lights on:  400410

    for x in range(1000):
        for y in range(1000):
            grid[x][y] = False
    for line in lines:
        grid = daySix.parseInstructionsPart2(line, grid)
    print "Total brightness: ", daySix.totalBrightness(grid)
#     Total brightness:  15343601
