'''
Created on 21 Dec 2015

@author: glucy
'''


# hlf r sets register r to half its current value, then continues with the next instruction.
# tpl r sets register r to triple its current value, then continues with the next instruction.
# inc r increments register r, adding 1 to it, then continues with the next instruction.
# jmp offset is a jump; it continues with the instruction offset away relative to itself.
# jie r, offset is like jmp, but only jumps if register r is even ("jump if even").
# jio r, offset is like jmp, but only jumps if register r is 1 ("jump if one", not odd).

class register():
    name = ''
    value = 0

    def __init__(self, name, value):
        self.name = name
        self.value = value

# Part 1 a start at 0
a = register('a', 0)
# Part 2 a starts at 1
# a = register('a', 1)
b = register('b', 0)

instructionList = list()


def executeInstruction(instruction, register, value, count):
    if instruction == 'hlf':
        register.value = register.value / 2
        count += 1
        return register, count
    if instruction == 'tpl':
        register.value = register.value * 3
        count += 1
        return register, count
    if instruction == 'inc':
        register.value += 1
        count += 1
        return register, count
    if instruction == 'jmp':
        count += int(value)
        return count
    if instruction == 'jie':
        if register.value % 2 == 0:
            count += int(value)
        else:
            count += 1
        return register, count
    if instruction == 'jio':
        if register.value == 1:
            count += int(value)
        else:
            count += 1
        return register, count


with open("/Users/glucy/code/AdventOfCode/resources/adventofcode/dayTwentyThree", "r") as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip('\n')
        line = line.replace(',', '')
        print line
        lineSplit = line.split()
        if lineSplit[0] in ['hlf', 'tpl', 'inc']:
            instructionList.append((lineSplit[0], lineSplit[1], ''))
        elif lineSplit[0] == 'jmp':
            instructionList.append((lineSplit[0], '', lineSplit[1]))
        else:
            instructionList.append((lineSplit[0], lineSplit[1], lineSplit[2]))

count = 0
while count < len(instructionList):
    inst = instructionList[count]
    if inst[1] == 'a':
        a, count = executeInstruction(inst[0], a, inst[2], count)
    elif inst[1] == 'b':
        b, count = executeInstruction(inst[0], b, inst[2], count)
    else:
        count = executeInstruction(inst[0], '', inst[2], count)

print "b.value: ", b.value
# Part 1: 170
# Part 2: 247
