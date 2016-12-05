import random
from decimal import Decimal
import math
import configparser
import statistics
from matplotlib import pyplot
import numpy

Config = configparser.ConfigParser()
Config.read('config.txt')
c1 = Config.getfloat('Main', '1')
c2 = Config.getfloat('Main', '2')
c3 = Config.getfloat('Main', '3')
c4 = Config.getfloat('Main', '4')
c5 = Config.getfloat('Main', '5')
c6 = Config.getfloat('Main', '6')
c8 = Config.getfloat('Main', '8')
c9 = Config.getfloat('Main', '9')
c10 = Config.getfloat('Main', '10')
c11 = Config.getfloat('Main', '11')
c12 = Config.getfloat('Main', '12')
c13 = Config.getfloat('Main', '13')
c14 = Config.getfloat('Main', '14')
c15 = Config.getfloat('Main', '15')
c17 = Config.getfloat('Main', '17')
brazilsim = Config.getboolean('Main', 'brazil')

print(brazilsim)


class Driver:

    def __init__(
        self,
        startpoints,
        brazil,
        abudhabi,
        points,
        ):
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

if brazilsim == True:
    for x in range(0, 1000):
        r = random.uniform(0, 99)
        r = math.ceil(r * 100) / 100
        print(r)
        if r > 0 and r <= 3.57:
            print('c1')
            case = 1
            rosberg.brazil = 25
            hamilton.brazil = 0
        elif r > 3.57 and r <= 37.5:
            print('c2')
            case = 2
            rosberg.brazil = 18
            hamilton.brazil = 25
        elif r > 37.5 and r <= 57.14:
            print('c3')
            case = 3
            rosberg.brazil = 25
            hamilton.brazil = 18
        elif r > 57.14 and r <= 60.71:
            print('c4')
            case = 4
            rosberg.brazil = 18
            hamilton.brazil = 0
        elif r > 60.71 and r <= 69.64:
            print('c5')
            case = 5
            rosberg.brazil = 0
            hamilton.brazil = 25
        elif r > 69.64 and r <= 80.35:
            print('c6')
            case = 6
            rosberg.brazil = 25
            hamilton.brazil = 15
        elif r > 80.35 and r <= 82.14:
            print('c8')
            case = 8
            rosberg.brazil = 25
            hamilton.brazil = 6
        elif r > 82.14 and r <= 83.93:
            print('c9')
            case = 9
            rosberg.brazil = 0
            hamilton.brazil = 0
        elif r > 83.93 and r <= 85.72:
            print('c10')
            case = 10
            rosberg.brazil = 6
            hamilton.brazil = 25
        elif r > 85.72 and r <= 87.51:
            print('c11')
            case = 11
            rosberg.brazil = 10
            hamilton.brazil = 25
        elif r > 87.51 and r <= 89.3:
            print('c12')
            case = 12
            rosberg.brazil = 25
            hamilton.brazil = 10
        elif r > 89.3 and r <= 92.87:
            print('c13')
            case = 13
            rosberg.brazil = 12
            hamilton.brazil = 25
        elif r > 92.87 and r <= 96.44:
            print('c14')
            case = 14
            rosberg.brazil = 15
            hamilton.brazil = 25
        elif r > 96.44 and r <= 98.23:
            print('c15')
            case = 15
            rosberg.brazil = 15
            hamilton.brazil = 18
        elif r > 98.23 and r <= 100.02:
            print('c17')
            case = 17
            rosberg.brazil = 12
            hamilton.brazil = 0

        r = random.uniform(0, 99)
        r = math.ceil(r * 100) / 100
        print(r)
        if r > 0 and r <= 3.64:
            print('c1')
            case = 1
            rosberg.abudhabi = 25
            hamilton.abudhabi = 0
        elif r > 3.64 and r <= 36.37:
            print('c2')
            case = 2
            rosberg.abudhabi = 18
            hamilton.abudhabi = 25
        elif r > 36.37 and r <= 56.37:
            print('c3')
            case = 3
            rosberg.abudhabi = 25
            hamilton.abudhabi = 18
        elif r > 56.37 and r <= 60.01:
            print('c4')
            case = 4
            rosberg.abudhabi = 18
            hamilton.abudhabi = 0
        elif r > 60.01 and r <= 69.1:
            print('c5')
            case = 5
            rosberg.abudhabi = 0
            hamilton.abudhabi = 25
        elif r > 69.1 and r <= 80.01:
            print('c6')
            case = 6
            rosberg.abudhabi = 25
            hamilton.abudhabi = 15
        elif r > 80.01 and r <= 81.83:
            print('c8')
            case = 8
            rosberg.abudhabi = 25
            hamilton.abudhabi = 6
        elif r > 81.83 and r <= 83.65:
            print('c9')
            case = 9
            rosberg.abudhabi = 0
            hamilton.abudhabi = 0
        elif r > 83.65 and r <= 85.47:
            print('c10')
            case = 10
            rosberg.abudhabi = 6
            hamilton.abudhabi = 25
        elif r > 85.47 and r <= 87.29:
            print('c11')
            case = 11
            rosberg.abudhabi = 10
            hamilton.abudhabi = 25
        elif r > 87.29 and r <= 89.11:
            print('c12')
            case = 12
            rosberg.abudhabi = 25
            hamilton.abudhabi = 10
        elif r > 89.11 and r <= 92.75:
            case = 13
            rosberg.abudhabi = 12
            hamilton.abudhabi = 25
        elif r > 92.75 and r <= 96.39:
            print('c14')
            case = 14
            rosberg.abudhabi = 15
            hamilton.abudhabi = 25
        elif r > 96.39 and r <= 98.21:
            print('c15')
            case = 15
            rosberg.abudhabi = 15
            hamilton.abudhabi = 18
        elif r > 98.21 and r <= 100.03:
            print('c17')
            case = 17
            rosberg.abudhabi = 12
            hamilton.abudhabi = 0

        rosberg.points = rosberg.startpoints + rosberg.brazil \
            + rosberg.abudhabi
        hamilton.points = hamilton.startpoints + hamilton.brazil \
            + hamilton.abudhabi

        roslist.append(rosberg.points)
        hamlist.append(hamilton.points)
elif brazilsim == False:
    for x in range(0, 100000):
        rosberg.brazil = 18
        hamilton.brazil = 25

        r = random.uniform(0, 99)
        r = math.ceil(r * 100) / 100
        print(r)
        if r > 0 and r <= 3.64:
            print('c1')
            case = 1
            rosberg.abudhabi = 25
            hamilton.abudhabi = 0
        elif r > 3.64 and r <= 36.37:
            print('c2')
            case = 2
            rosberg.abudhabi = 18
            hamilton.abudhabi = 25
        elif r > 36.37 and r <= 56.37:
            print('c3')
            case = 3
            rosberg.abudhabi = 25
            hamilton.abudhabi = 18
        elif r > 56.37 and r <= 60.01:
            print('c4')
            case = 4
            rosberg.abudhabi = 18
            hamilton.abudhabi = 0
        elif r > 60.01 and r <= 69.1:
            print('c5')
            case = 5
            rosberg.abudhabi = 0
            hamilton.abudhabi = 25
        elif r > 69.1 and r <= 80.01:
            print('c6')
            case = 6
            rosberg.abudhabi = 25
            hamilton.abudhabi = 15
        elif r > 80.01 and r <= 81.83:
            print('c8')
            case = 8
            rosberg.abudhabi = 25
            hamilton.abudhabi = 6
        elif r > 81.83 and r <= 83.65:
            print('c9')
            case = 9
            rosberg.abudhabi = 0
            hamilton.abudhabi = 0
        elif r > 83.65 and r <= 85.47:
            print('c10')
            case = 10
            rosberg.abudhabi = 6
            hamilton.abudhabi = 25
        elif r > 85.47 and r <= 87.29:
            print('c11')
            case = 11
            rosberg.abudhabi = 10
            hamilton.abudhabi = 25
        elif r > 87.29 and r <= 89.11:
            print('c12')
            case = 12
            rosberg.abudhabi = 25
            hamilton.abudhabi = 10
        elif r > 89.11 and r <= 92.75:
            print('c13')
            case = 13
            rosberg.abudhabi = 12
            hamilton.abudhabi = 25
        elif r > 92.75 and r <= 96.39:
            print('c14')
            case = 14
            rosberg.abudhabi = 15
            hamilton.abudhabi = 25
        elif r > 96.39 and r <= 98.21:
            print('c15')
            case = 15
            rosberg.abudhabi = 15
            hamilton.abudhabi = 18
        elif r > 98.21 and r <= 100.03:
            print('c17')
            case = 17
            rosberg.abudhabi = 12
            hamilton.abudhabi = 0

        rosberg.points = rosberg.startpoints + rosberg.brazil \
            + rosberg.abudhabi
        hamilton.points = hamilton.startpoints + hamilton.brazil \
            + hamilton.abudhabi

        roslist.append(rosberg.points)
        hamlist.append(hamilton.points)

for x in range(0, len(roslist)):
    if roslist[x] > hamlist[x]:
        roswins = roswins + 1
    elif hamlist[x] > roslist[x]:
        hamwins = hamwins + 1
    elif hamlist[x] == roslist[x]:
        ties = ties + 1

print('rosberg:' + str(roswins))
print('hamilton:' + str(hamwins))
print('ties:' + str(ties))

print()
print()

print('rosberg mean:' + str(statistics.mean(roslist)))
print('rosberg median:' + str(statistics.median(roslist)))
print('rosberg std. dev:' + str(statistics.stdev(roslist)))

print()
print()

print('hamilton mean:' + str(statistics.mean(hamlist)))
print('hamilton median:' + str(statistics.median(hamlist)))
print('hamilton std. dev:' + str(statistics.stdev(hamlist)))

f = open('results.txt','w')
f.write('rosberg:' + str(roswins) + '\n')
f.write('hamilton:' + str(hamwins) + '\n')
f.write('ties:' + str(ties) + '\n')

f.write('\n')

f.write('rosberg mean:' + str(statistics.mean(roslist)) + '\n')
f.write('rosberg median:' + str(statistics.median(roslist)) + '\n')
f.write('rosberg std. dev:' + str(statistics.stdev(roslist)) + '\n')

f.write('\n')

f.write('hamilton mean:' + str(statistics.mean(hamlist)) + '\n')
f.write('hamilton median:' + str(statistics.median(hamlist)) + '\n')
f.write('hamilton std. dev:' + str(statistics.stdev(hamlist)) + '\n')

f.close()

bins = numpy.linspace(330, 399, 18)
pyplot.hist(roslist, bins, alpha=0.5, label='rosberg')
pyplot.hist(hamlist, bins, alpha=0.5, label='hamilton')
pyplot.legend(loc='upper right')
pyplot.show()
