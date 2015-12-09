'''
Created on 8 Dec 2015

@author: glucy
'''


class DayEight():

    def __init__(self):
        pass


def charactorsOfCode(line):
    line = line.rstrip("\n")
    print "charactorsOfCode: ", line
    print "charactorsOfCode num: ", len(line)
    return len(line)


def stringDataDecode(line):
    line = line.rstrip("\n")
    line = line.decode('string_escape')
    print "decode: ", line
    line = line[1:-1]
    print "stringDataDecode: ", line
    print "stringDataDecode num: ", len(line)
    return len(line)


def stringDataEncode(line):
    line = line.rstrip("\n")
    line = "\"" + line
    line += "\""
    print "added quotes: ", line
    line = line.encode('string_escape')
    print "encode: ", line
    print "stringDataEncode: ", line
    print "stringDataEncode num: ", len(line)
    return len(line)

with open("/Users/glucy/code/AdventOfCode/resources/adventofcode/dayEight", "r") as f:
    dayEight = DayEight()
    lines = f.readlines()
    numCharactorsOfCode = 0
    numStringDataDecode = 0

    for line in lines:
        numCharactorsOfCode += charactorsOfCode(line)
        numStringDataDecode += stringDataDecode(line)

    print "numCharactorsOfCode: ", numCharactorsOfCode
    print "numStringDataDEcode: ", numStringDataDecode
    print "Part 1: numCharactorsOfCode  - numStringData: ", (numCharactorsOfCode - numStringDataDecode)

encoded, literal = 0, 0

with open("/Users/glucy/code/AdventOfCode/resources/adventofcode/dayEight", "r") as f:
    rows = f.read().splitlines()

for line in rows:
    extra = 4
    for char in line[1:-1]:
        if char == "\\" or char == '"':
            extra += 1

    encoded += len(line) + extra
    literal += len(line)

print "Part 2: ", encoded - literal
