'''
Created on 13 Dec 2015

@author: glucy
'''
# Dancer can fly 27 km/s for 5 seconds, but then must rest for 132 seconds.
# Cupid can fly 22 km/s for 2 seconds, but then must rest for 41 seconds.
# Rudolph can fly 11 km/s for 5 seconds, but then must rest for 48 seconds.
# Donner can fly 28 km/s for 5 seconds, but then must rest for 134 seconds.
# Dasher can fly 4 km/s for 16 seconds, but then must rest for 55 seconds.
# Blitzen can fly 14 km/s for 3 seconds, but then must rest for 38 seconds.
# Prancer can fly 3 km/s for 21 seconds, but then must rest for 40 seconds.
# Comet can fly 18 km/s for 6 seconds, but then must rest for 103 seconds.
# Vixen can fly 18 km/s for 5 seconds, but then must rest for 84 seconds.


class Reindeer():

    name = ''
    speed = 0
    duration = 0
    rest = 0
    totalDistance = 0
    points = 0

    def __init__(self, name, speed, duration, rest):
        self.name = name
        self.speed = speed
        self.duration = duration
        self.rest = rest


with open("/Users/glucy/code/AdventOfCode/resources/adventofcode/dayFourteen", "r") as f:
    lines = f.readlines()
    reindeers = list()
    for line in lines:
        line = line[:-2]
        name, _, _, speed, _, _, duration, _, _, _, _, _, _, rest, _ = line.split()
        reindeers.append(Reindeer(name, int(speed), int(duration), int(rest)))


def totalDistanceIn(reindeer, seconds):
    totalTime = 0
    while totalTime + reindeer.duration <= seconds:
        reindeer.totalDistance += reindeer.speed * reindeer.duration
        totalTime += reindeer.duration
        totalTime += reindeer.rest
        if totalTime > seconds:
            break
        elif totalTime + reindeer.duration >= seconds:
            leftOverTime = seconds - totalTime
            reindeer.totalDistance += reindeer.speed * leftOverTime
            totalTime += leftOverTime
    if reindeer.totalDistance == 0:
        leftOverTime = seconds - totalTime
        reindeer.totalDistance += reindeer.speed * leftOverTime
    return reindeer

# PART 1
reindeerList1 = reindeers
reindeerList2 = reindeers
raceTime = 2503
winningDistance = 0
for deer in reindeerList1:
    deer = totalDistanceIn(deer, raceTime)
    distance = deer.totalDistance
    if distance > winningDistance:
        winningDistance = distance

print "Winning Distance: ", winningDistance


# PART 2
winningPoints = 0
sec = 1
while sec <= raceTime:
    leaderSet = set()
    currentLeader = Reindeer("blank", 0, 0, 0)
    for deer in reindeerList2:
        deer.totalDistance = 0
        deer = totalDistanceIn(deer, sec)
    for deer in reindeerList2:
        if deer.totalDistance > currentLeader.totalDistance:
            leaderSet.clear()
            leaderSet.add(deer)
            currentLeader = deer
        elif deer.totalDistance == currentLeader.totalDistance:
            leaderSet.add(deer)
            leaderSet.add(currentLeader)
    for deer in leaderSet:
        deer.points += 1
    sec += 1
for deer in reindeerList2:
    if deer.points > winningPoints:
        winningPoints = deer.points

print "Winning Points: ", winningPoints
