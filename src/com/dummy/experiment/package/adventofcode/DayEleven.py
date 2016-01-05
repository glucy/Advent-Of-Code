'''
Created on 11 Dec 2015

@author: glucy
'''


def straightOfThree(password):
    i = 0
    while i < len(password) - 3:
        if (ord(password[i]) + 1 == ord(password[i + 1]) and
                ord(password[i + 1]) + 1 == ord(password[i + 2])):
                return True
        else:
            i += 1
    return False
# print "straightOfThree(\"hijklmmn\"): ", straightOfThree("hijklmmn")
# print "straightOfThree(\"adccpuxw\"): ", straightOfThree("adccpuxw")


def invalidChar(password):
    if "i" in password or "l" in password or "o" in password:
        return False
    return True
# print "invalidChar(\"hijklmmn\"): ", invalidChar("hijklmmn")
# print "invalidChar(\"adccpuxw\"): ", invalidChar("adccpuxw")


def twoPairs(password):
    i = 0
    pairs = 0
    while i < len(password) - 1:
        if password[i] == password[i + 1]:
            pairs += 1
            i += 1
        else:
            i += 1

    j = 0
    while j < len(password) - 2:
        if password[j] == password[j + 1] and password[j] == password[j + 2]:
            pairs -= 1
            j += 1
        else:
            j += 1

    if pairs >= 2:
        return True
    return False
# print "twoPairs(\"abbcefgg\"): ", twoPairs("abbcefgg")
# print "twoPairs(\"abbcefkg\"): ", twoPairs("abbcefkg")
# print "twoPairs(\"abbbcefg\"): ", twoPairs("abbbcefg")


def validPassword(password):
    if straightOfThree(password) and invalidChar(password) and twoPairs(password):
        return True
    return False


def incrementPassword(password):
    password[-1] = 'a' if ord(password[-1]) + 1 > ord('z') else chr(ord(password[-1]) + 1)
    return password if password[-1] != 'a' else incrementPassword(password[:-1]) + ['a']


def newPassword(oldPassword):
    password = incrementPassword(oldPassword)
    while not validPassword(password):
        password = incrementPassword(password)
    return password


inputValue = "hepxcrrq"
inputValue = ''.join(newPassword(list(inputValue)))
print "Phase 1: ", inputValue
# Phase 1:  hepxxyzz
inputValue = ''.join(newPassword(list(inputValue)))
print "Phase 2: ", inputValue
# Phase 2:  heqaabcc
