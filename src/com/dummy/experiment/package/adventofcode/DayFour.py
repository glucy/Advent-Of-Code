'''
Created on 3 Dec 2015

@author: glucy
'''
import hashlib


class DayFour():

    count = 0

    def __init__(self):
        pass

    def parseResultForFiveZeros(self, md5Hash):
        if md5Hash[:5] == "00000":
            return True
        return False

    def parseResultForSixZeros(self, md5Hash):
        if md5Hash[:6] == "000000":
            return True
        return False

    def generateMD5Hash(self, count, inputValue):
        m = hashlib.md5()
        m.update(inputValue)
        m.update(str(count))
        md5Hash = m.hexdigest()
        return md5Hash

    def findTheSmallestFiveZero(self, inputValue):
        while self.parseResultForFiveZeros(self.generateMD5Hash(self.count, inputValue)) == False:
            self.count += 1
        print "MD5 Hash Five Zero: ", self.generateMD5Hash(self.count, inputValue)
        return self.count

    def findTheSmallestSixZero(self, inputValue):
        while self.parseResultForSixZeros(self.generateMD5Hash(self.count, inputValue)) == False:
            self.count += 1
        print "MD5 Hash Six Zero: ", self.generateMD5Hash(self.count, inputValue)
        return self.count

inputValue = "bgvyzdsv"
dayFour = DayFour()
SamllestNum = dayFour.findTheSmallestFiveZero(inputValue)
print "SamllestNum5: ", SamllestNum
dayFour = DayFour()
SamllestNum = dayFour.findTheSmallestSixZero(inputValue)
print "SamllestNum6: ", SamllestNum
