'''
Created on 10 Dec 2015

@author: glucy
'''


def countChars(inputVal):
    length = len(inputVal)
    i = 0
    j = 0
    counter = 1
    output = []
    while i < length:
        while j < length - 1:
            if inputVal[i] == inputVal[j + 1]:
                counter += 1
                j += 1
            else:
                output.append(counter)
                output.append(inputVal[i])
                counter = 1
                i = j + 1
                j = i
                break
        if j + 1 == length:
            output.append(counter)
            output.append(inputVal[i])
            i = j + 1
    return output

inputNums = [1, 1, 1, 3, 2, 2, 2, 1, 1, 3]
x = 0
while x < 40:
    inputNums = countChars(inputNums)
    x += 1

print "40 Times: ", len(inputNums)
# 40 Times:  252594

inputNums = [1, 1, 1, 3, 2, 2, 2, 1, 1, 3]
x = 0
while x < 50:
    inputNums = countChars(inputNums)
    x += 1

print "50 Times:", len(inputNums)
# 50 Times: 3579328
