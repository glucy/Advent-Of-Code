'''
Created on 5 Dec 2015

@author: glucy
'''


class DayFive():

    def __init__(self):
        pass

    def containsThreeVowels(self, input):
        count = 0
        for c in input:
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

    def containsDoubleLetter(self, input):
        i = 0
        while i < len(input) - 1:
            if input[i] == input[i + 1]:
                return True
            else:
                i += 1
        return False

    def doesNotContainsBadLetters(self, input):
        # Bad Strings: ab, cd, pq, or xy
        if 'ab' not in input and 'cd' not in input and 'pq' not in input and 'xy' not in input:
            return True
        return False

    def repeatingLetterWithOneBetween(self, input):
        i = 0
        while i < len(input) - 2:
            if input[i] == input[i + 2]:
                return True
            else:
                i += 1
        return False

    def pairOfLettersAppearingTwice(self, input):
        i = 0
        while i < len(input) - 2:
            if input[i:i + 2] in input[i + 2:]:
                return True
            else:
                i += 1
        return False

with open("/Users/glucy/code/AdventOfCode/resources/adventofcode/dayFive", "r") as f:
    dayFive = DayFive()
    count = 0
    listOfLines = f.readlines()
    for word in listOfLines:
        if dayFive.containsThreeVowels(word) and dayFive.containsDoubleLetter(word) and dayFive.doesNotContainsBadLetters(word):
            count += 1

    print "Nice Words Part One: ", count

    num = 0
    for line in listOfLines:
        if dayFive.repeatingLetterWithOneBetween(line) and dayFive.pairOfLettersAppearingTwice(line):
            num += 1

    print "Nice Words Part Two:", num
