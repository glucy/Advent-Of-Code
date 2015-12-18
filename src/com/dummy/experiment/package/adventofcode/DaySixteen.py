'''
Created on 16 Dec 2015

@author: glucy
'''


# Sue 1: goldfish: 6, trees: 9, akitas: 0
# Sue 2: goldfish: 7, trees: 1, akitas: 0


from collections import defaultdict


key = {"children": 3,
        "cats": 7,
        "samoyeds": 2,
        "pomeranians": 3,
        "akitas": 0,
        "vizslas": 0,
        "goldfish": 5,
        "trees": 3,
        "cars": 2,
        "perfumes": 1}


def equal(a, b):
    return all(item in b and b[item] == a[item] for item in a)


def equals(a, b):
    isAuntie = False
    for item in a:
        if item in b and a[item] == b[item]:
            isAuntie = True
        else:
            isAuntie = False
            break
    return isAuntie


def equal_real(a, b):
    for item in a:
        if item in ["cats", "trees"]:
            if a[item] <= b[item]:
                return False
        elif item in ["pomeranians", "goldfish"]:
            if a[item] >= b[item]:
                return False
        elif b[item] != a[item]:
            return False
    return True


def equals_real(a, b):
    isAuntie = False
    for item in a:
        if item in ["cats", "trees"]:
            if a[item] > b[item]:
                isAuntie = True
            elif item in ["pomeranians", "goldfish"]:
                if a[item] < b[item]:
                    isAuntie = True
            elif a[item] == b[item]:
                isAuntie = True
            else:
                isAuntie = False
                break
    return isAuntie


def find_sue(data, key, equal_function):
    for sue in data:
        if equal_function(data[sue], key):
            return sue
    return None


with open("/Users/glucy/code/AdventOfCode/resources/adventofcode/daySixteen", "r") as f:
    lines = f.readlines()

    data = defaultdict(dict)
    for line in lines:
        line = line.split()
        sue = line[1]
        line = line[2:]
        for i in range(len(line)//2):
            item = line[2*i].strip(',').strip(':')
            value = line[2*i+1].strip(',')
            data[sue][item] = int(value)

    print(find_sue(data, key, equals))
    print(find_sue(data, key, equal_real))
