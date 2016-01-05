'''
Created on 17 Dec 2015

@author: glucy
'''

import itertools


listOfJars = [11, 30, 47, 31, 32, 36, 3, 1, 5, 3, 32, 36, 15, 11, 46, 26, 28, 1, 19, 3]

total = 0
for i in range(1, len(listOfJars)):
    print "Number of Jars to use: ", i
    subtotal = 0
    for combination in itertools.combinations(listOfJars, i):
        if sum(combination) == 150:
            subtotal += 1
    total += subtotal
    print "Number of combinations: ", subtotal
print "Total number of combinations: ", total
