import random
from decimal import Decimal
import math

class Driver:
    def __init__(self, startpoints, brazil, abudhabi, points):
        self.startpoints = startpoints
        self.brazil = brazil
        self.abudhabi = abudhabi
        self.points = points

rosberg = Driver(349, 0, 0, 0)
hamilton = Driver(330, 0, 0, 0)

hamlist = []
roslist = []

roswins = 0
hamwins = 0
ties = 0

drivers = [rosberg, hamilton]
case = None


for x in range(0, 1000):
    r = random.uniform(0, 99)
    r = math.ceil(r*100)/100
    print(r)
    if r > 0 and r <= 3.64:#case 1:
        print("c1")
        case = 1
        rosberg.brazil = 25
        hamilton.brazil = 0
    elif r > 3.64 and r <= 36.37:#case 2:
        print("c2")
        case = 2
        rosberg.brazil = 18
        hamilton.brazil = 25
    elif r > 36.37 and r <= 56.37:#case 3:
        print("c3")
        case = 3
        rosberg.brazil = 25
        hamilton.brazil = 18
    elif r > 56.37 and r <= 60.01:#case 4:
        print("c4")
        case = 4
        rosberg.brazil = 18
        hamilton.brazil = 0
    elif r > 60.01 and r <= 69.1:#case 5:
        print("c5")
        case = 5
        rosberg.brazil = 0
        hamilton.brazil = 25
    elif r > 69.1 and r <= 80.01:#case 6: 105
        print("c6")
        case = 6
        rosberg.brazil = 25
        hamilton.brazil = 15
    elif r > 80.01 and r <= 81.83:#case 8: 17
        print("c8")
        case = 8
        rosberg.brazil = 25
        hamilton.brazil = 6
    elif r > 81.83 and r <= 83.65:#case 9: 17
        print("c9")
        case = 9
        rosberg.brazil = 0
        hamilton.brazil = 0
    elif r > 83.65 and r <= 85.47:#case 10: 17
        print("c10")
        case = 10
        rosberg.brazil = 6
        hamilton.brazil = 25
    elif r > 85.47 and r <= 87.29:#case 11: 17
        print("c11")
        case = 11
        rosberg.brazil = 10
        hamilton.brazil = 25
    elif r > 87.29 and r <= 89.11:#case 12: 17
        print("c12")
        case = 12
        rosberg.brazil = 25
        hamilton.brazil = 10
    elif r > 89.11 and r <= 92.75:#case 13: 35
        print("c13")
        case = 13
        rosberg.brazil = 12
        hamilton.brazil = 25
    elif r > 92.75 and r <= 96.39:#case 14: 35
        print("c14")
        case = 14
        rosberg.brazil = 15
        hamilton.brazil = 25
    elif r > 96.39 and r <= 98.21:#case 15: 17
        print("c15")
        case = 15
        rosberg.brazil = 15
        hamilton.brazil = 18
    elif r > 98.21 and r <= 100.03:#case 17: 17
        print("c17")
        case = 17
        rosberg.brazil = 12
        hamilton.brazil = 0

    r = random.uniform(0, 99)#random for abudhabi
    r = math.ceil(r*100)/100
    print(r)
    if r > 0 and r <= 3.64:#case 1:
        print("c1")
        case = 1
        rosberg.abudhabi = 25
        hamilton.abudhabi = 0
    elif r > 3.64 and r <= 36.37:#case 2:
        print("c2")
        case = 2
        rosberg.abudhabi = 18
        hamilton.abudhabi = 25
    elif r > 36.37 and r <= 56.37:#case 3:
        print("c3")
        case = 3
        rosberg.abudhabi = 25
        hamilton.abudhabi = 18
    elif r > 56.37 and r <= 60.01:#case 4:
        print("c4")
        case = 4
        rosberg.abudhabi = 18
        hamilton.abudhabi = 0
    elif r > 60.01 and r <= 69.1:#case 5:
        print("c5")
        case = 5
        rosberg.abudhabi = 0
        hamilton.abudhabi = 25
    elif r > 69.1 and r <= 80.01:#case 6: 105
        print("c6")
        case = 6
        rosberg.abudhabi = 25
        hamilton.abudhabi = 15
    elif r > 80.01 and r <= 81.83:#case 8: 17
        print("c8")
        case = 8
        rosberg.abudhabi = 25
        hamilton.abudhabi = 6
    elif r > 81.83 and r <= 83.65:#case 9: 17
        print("c9")
        case = 9
        rosberg.abudhabi = 0
        hamilton.abudhabi = 0
    elif r > 83.65 and r <= 85.47:#case 10: 17
        print("c10")
        case = 10
        rosberg.abudhabi = 6
        hamilton.abudhabi = 25
    elif r > 85.47 and r <= 87.29:#case 11: 17
        print("c11")
        case = 11
        rosberg.abudhabi = 10
        hamilton.abudhabi = 25
    elif r > 87.29 and r <= 89.11:#case 12: 17
        print("c12")
        case = 12
        rosberg.abudhabi = 25
        hamilton.abudhabi = 10
    elif r > 89.11 and r <= 92.75:#case 13: 35
        print("c13")
        case = 13
        rosberg.abudhabi = 12
        hamilton.abudhabi = 25
    elif r > 92.75 and r <= 96.39:#case 14: 35
        print("c14")
        case = 14
        rosberg.abudhabi = 15
        hamilton.abudhabi = 25
    elif r > 96.39 and r <= 98.21:#case 15: 17
        print("c15")
        case = 15
        rosberg.abudhabi = 15
        hamilton.abudhabi = 18
    elif r > 98.21 and r <= 100.03:#case 17: 17
        print("c17")
        case = 17
        rosberg.abudhabi = 12
        hamilton.abudhabi = 0

    rosberg.points = rosberg.startpoints + rosberg.brazil + rosberg.abudhabi
    hamilton.points = hamilton.startpoints + hamilton.brazil + hamilton.abudhabi

    roslist.append(rosberg.points)
    hamlist.append(hamilton.points)

for x in range(0, len(roslist)):
    if roslist[x] > hamlist[x]:
        roswins = roswins + 1
    elif hamlist[x] > roslist[x]:
        hamwins = hamwins + 1
    elif hamlist[x] == roslist[x]:
        ties = ties + 1

print("rosberg:" + str(roswins))
print("hamilton:" + str(hamwins))
print("ties:" + str(ties))
