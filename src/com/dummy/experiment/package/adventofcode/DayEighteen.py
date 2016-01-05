'''
Created on 18 Dec 2015

@author: glucy
'''


def howManyNeighboursAreOn(lights, x, y):
    count = 0
    # Left Middle
    if x - 1 >= 0 and lights[x - 1][y] == '#':
        count += 1
    # Bottom Left
    if x - 1 >= 0 and y - 1 >= 0 and lights[x - 1][y - 1] == '#':
        count += 1
    # Top Left
    if x - 1 >= 0 and y + 1 < 100 and lights[x - 1][y + 1] == '#':
        count += 1
    # Right Middle
    if x + 1 < 100 and lights[x + 1][y] == '#':
        count += 1
    # Bottom Right
    if x + 1 < 100 and y - 1 >= 0 and lights[x + 1][y - 1] == '#':
        count += 1
    # Top Right
    if x + 1 < 100 and y + 1 < 100 and lights[x + 1][y + 1] == '#':
        count += 1
    # Top Middle
    if y + 1 < 100 and lights[x][y + 1] == '#':
        count += 1
    # Bottom Middle
    if y - 1 >= 0 and lights[x][y - 1] == '#':
        count += 1
    return count


def onOrOff(previousLights):
    nextLights = [[0 for i in range(100)] for i in range(100)]
    for x in range(0, 100):
        for y in range(0, 100):
            if previousLights[x][y] == '#' and howManyNeighboursAreOn(previousLights, x, y) in [2, 3]:
                nextLights[x][y] = '#'
            elif previousLights[x][y] == '.' and howManyNeighboursAreOn(previousLights, x, y) == 3:
                nextLights[x][y] = '#'
            # Below elif is for Part 2 Only
            elif (x == 0 and y == 0) or (x == 0 and y == 99) or (x == 99 and y == 0) or (x == 99 and y == 99):
                nextLights[x][y] = '#'
            else:
                nextLights[x][y] = '.'
    return nextLights


def howManySteps(lights, steps):
    i = 0
    while i < steps:
        lights = onOrOff(lights)
        i += 1
    return lights


def howManyOn(lights):
    j = 0
    for x in range(0, 100):
        for y in range(0, 100):
            if lights[x][y] == '#':
                j += 1
    return j


with open("/Users/glucy/code/AdventOfCode/resources/adventofcode/dayEighteen", "r") as f:
    lines = f.readlines()
    grid = [[0 for x in range(100)] for x in range(100)]
    x = 0
    y = 0
    for line in lines:
        line = line.strip('\n')
        for character in line:
            grid[x][y] = character
            y += 1
        x += 1
        y = 0

    # Part 2
#     grid[0][0] = '#'
#     grid[0][99] = '#'
#     grid[99][0] = '#'
#     grid[99][99] = '#'

    lightGrid = howManySteps(grid, 100)
    print howManyOn(lightGrid)
#     Part 1: 1061
#     Part 2: 1006
