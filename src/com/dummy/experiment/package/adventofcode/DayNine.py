'''
Created on 9 Dec 2015

@author: glucy
'''

import itertools


with open("/Users/glucy/code/AdventOfCode/resources/adventofcode/dayNine", "r") as f:
    lines = f.readlines()

    cities = set()
    dist = {}
    for line in lines:
        a, _, b, _, d = line.split(' ')
        cities.add(a)
        cities.add(b)
        dist[(a, b)] = int(d)
        dist[(b, a)] = int(d)

    def length(p):
        i = 0
        total = 0
        while i < len(p) - 1:
            total += dist[(p[i], p[i + 1])]
            i += 1
        return total

    min_dist = 9999999999
    max_dist = 0
    for perm in itertools.permutations(cities):
        perm_len = length(perm)
        if perm_len < min_dist:
            min_dist = perm_len
        if perm_len > max_dist:
            max_dist = perm_len
    print "Min Dist: ", min_dist
    print "MAx Dist: ", max_dist
