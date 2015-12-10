'''
Created on 5 Dec 2015

@author: glucy
'''


class DayFive():

    def __init__(self):
        pass

    def containsThreeVowels(self, inputVal):
        count = 0
        for c in inputVal:
            if c == 'a':
                count += 1
            elif c == 'e':
                count += 1
            elif c == 'i':
                count += 1
            elif c == 'o':
                count += 1
            elif c == 'u':
                count += 1

        if count >= 3:
            return True
        return False

    def containsDoubleLetter(self, inputVal):
        i = 0
        while i < len(inputVal) - 1:
            if inputVal[i] == inputVal[i + 1]:
                return True
            else:
                i += 1
        return False

    def doesNotContainsBadLetters(self, inputVal):
        # Bad Strings: ab, cd, pq, or xy
        if 'ab' not in inputVal and 'cd' not in inputVal and 'pq' not in inputVal and 'xy' not in inputVal:
            return True
        return False

    def repeatingLetterWithOneBetween(self, inputVal):
        i = 0
        while i < len(inputVal) - 2:
            if inputVal[i] == inputVal[i + 2]:
                return True
            else:
                i += 1
        return False

    def pairOfLettersAppearingTwice(self, inputVal):
        i = 0
        while i < len(inputVal) - 2:
            if inputVal[i:i + 2] in inputVal[i + 2:]:
                return True
            else:
                i += 1
        return False

with open("/Users/glucy/code/AdventOfCode/resources/adventofcode/dayFive", "r") as f:
    dayFive = DayFive()
    count = 0
    listOfLines = f.readlines()
    for word in listOfLines:
        if (dayFive.containsThreeVowels(word) and
                dayFive.containsDoubleLetter(word) and
                dayFive.doesNotContainsBadLetters(word)):

            count += 1

    print "Nice Words Part One: ", count

    num = 0
    for line in listOfLines:
        if dayFive.repeatingLetterWithOneBetween(line) and dayFive.pairOfLettersAppearingTwice(line):
            num += 1

    print "Nice Words Part Two: ", num
