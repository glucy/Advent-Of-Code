'''
Created on 12 Dec 2015

@author: glucy
'''

import re
import json


with open("/Users/glucy/code/AdventOfCode/resources/adventofcode/dayTwelve", "r") as f:
    line = f.readline()
print line
nums = []
nums = re.findall("[-+]?\d+[\.]?\d*", line)
print nums
total = 0
for i in nums:
    total += int(i)

print "Total Sum of all numbers: ", total


def sum_numbers(obj):
    if isinstance(obj, dict):
        if "red" in obj.values():
            return 0
        return sum(map(sum_numbers, obj.values()))

    if isinstance(obj, list):
        return sum(map(sum_numbers, obj))

    if isinstance(obj, int):
        return obj

    return 0

data = json.loads(line)
print data
print "Total Sum of all non-red numbers: ", sum_numbers(data)
