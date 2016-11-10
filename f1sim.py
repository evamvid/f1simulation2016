import random

class Driver:
    def __init__(self, startpoints, brazil, abudhabi, points):
        self.startpoints = startpoints
        self.brazil = brazil
        self.abudhabi = abudhabi
        self.points = points

rosberg = Driver(349, 0, 0, 0)
hamilton = Driver(330, 0, 0, 0)

drivers = [rosberg, hamilton]
case = None


for x in range(0, 1000):
    r = random.randrange(0, 999)
    if r > 0 & r <= 35:#case 1:
        print("c1")
        case = 1
        rosberg.brazil = 25
        hamilton.brazil = 0
    elif r > 36 & r <= 364:#case 2:
        print("c2")
        case = 2
        rosberg.brazil = 18
        hamilton.brazil = 25
    elif r > 365 & r <= 565:#case 3:
        print("c3")
        case = 3
        rosberg.brazil = 25
        hamilton.brazil = 18
    elif r > 566 & r <= 602:#case 4:
        print("c4")
        case = 4
        rosberg.brazil = 18
        hamilton.brazil = 0
    elif r > 603 & r <= 693:#case 5:
        print("c5")
        case = 5
        rosberg.brazil = 0
        hamilton.brazil = 25
    elif r > 694 & r <= 803:#case 6: 105
        print("c6")
        case = 6
        rosberg.brazil = 25
        hamilton.brazil = 15
    elif r > 804 & r <= 822:#case 8: 17
        print("c8")
        case = 8
        rosberg.brazil = 25
        hamilton.brazil = 6
    elif r > 823 & r <= 841:#case 9: 17
        print("c9")
        case = 9
        rosberg.brazil = 0
        hamilton.brazil = 0
    elif r > 842 & r <= 860:#case 10: 17
        print("c10")
        case = 10
        rosberg.brazil = 6
        hamilton.brazil = 25
    elif r > 861 & r <= 879:#case 11: 17
        print("c11")
        case = 11
        rosberg.brazil = 10
        hamilton.brazil = 25
    elif r > 880 & r <= 898:#case 12: 17
        print("c12")
        case = 12
        rosberg.brazil = 25
        hamilton.brazil = 10
    elif r > 899 & r <= 935:#case 13: 35
        print("c13")
        case = 13
        rosberg.brazil = 12
        hamilton.brazil = 25
    elif r > 936 & r <= 972:#case 14: 35
        print("c14")
        case = 14
        rosberg.brazil = 15
        hamilton.brazil = 25
    elif r > 973 & r <= 991:#case 15: 17
        print("c15")
        case = 15
        rosberg.brazil = 15
        hamilton.brazil = 18
    elif r > 992 & r <= 1010:#case 17: 17
        print("c17")
        case = 17
        rosberg.brazil = 12
        hamilton.brazil = 0
