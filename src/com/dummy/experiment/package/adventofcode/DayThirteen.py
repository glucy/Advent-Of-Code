'''
Created on 13 Dec 2015

@author: glucy
'''


import itertools

# Alice would gain 54 happiness units by sitting next to Bob.


with open("/Users/glucy/code/AdventOfCode/resources/adventofcode/dayThirteen", "r") as f:
    lines = f.readlines()
    people = set()
    happiness = {}
    for line in lines:
        line = line[:-2]
        a, _, pn, h, _, _, _, _, _, _, b = line.split(' ')
        people.add(a)
        people.add(b)
        if pn == "gain":
            happiness[(a, b)] = int(h)
        else:
            happiness[(a, b)] = -int(h)
# Uncomment for Part 2:
            happiness[("me", a)] = 0
            happiness[(a, "me")] = 0
    people.add("me")

    print "people: ", people
    print "happiness: ", happiness

    max_happiness = 0
    for seating in itertools.permutations(people):
        h = 0
        for i in xrange(len(seating)):
            a, b = seating[i-1], seating[i]
            h += happiness[(a, b)] + happiness[(b, a)]

        if h > max_happiness:
            max_happiness = h
    print "max_happiness: ", max_happiness
