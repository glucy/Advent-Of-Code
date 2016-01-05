from functools import reduce
from itertools import combinations
from operator import mul

wts = list()
with open("/Users/glucy/code/AdventOfCode/resources/adventofcode/dayTwentyFour", "r") as f:
    lines = f.readlines()
    for line in lines:
        wts.append(int(line.strip()))


def day24(num_groups):
    group_size = sum(wts) // num_groups
    for i in range(len(wts)):
        qes = [reduce(mul, c) for c in combinations(wts, i) if sum(c) == group_size]
        if qes:
            return min(qes)

print(day24(3))
print(day24(4))
