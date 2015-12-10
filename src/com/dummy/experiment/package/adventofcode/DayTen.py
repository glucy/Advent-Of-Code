'''
Created on 10 Dec 2015

@author: glucy
'''


def countChars(input):
    length = len(input)
    i = 0
    j = 0
    counter = 1
    output = []
    while i < length:
        while j < length - 1:
            if input[i] == input[j + 1]:
                counter += 1
                j += 1
            else:
                output.append(counter)
                output.append(input[i])
                counter = 1
                i = j + 1
                j = i
                break
        if j + 1 == length:
            output.append(counter)
            output.append(input[i])
            i = j + 1
    return output

input = [1, 1, 1, 3, 2, 2, 2, 1, 1, 3]
x = 0
while x < 40:
    input = countChars(input)
    x += 1

print "40 Times: ", len(input)

input = [1, 1, 1, 3, 2, 2, 2, 1, 1, 3]
x = 0
while x < 50:
    input = countChars(input)
    x += 1

print "50 Times:", len(input)

