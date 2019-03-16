class Game:
    def __init__(self):
        self.round = 0
        self.throwNumber = 0

    def computeNumberCount(self, beaker, number):
        count = 0
        for die in beaker:
            if beaker.dice[die][1] == number:
                count += beaker.dice[die][1]
        return count

    def computeStairway(self, beaker):
        testBeaker1 = [["die1", 1, "unlocked"], ["die2", 2, "unlocked"], ["die3", 3, "unlocked"],
                       ["die4", 4, "unlocked"], ["die5", 5, "unlocked"]]
        testBeaker2 = [["die1", 2, "unlocked"], ["die2", 3, "unlocked"], ["die3", 4, "unlocked"],
                       ["die4", 5, "unlocked"], ["die5", 6, "unlocked"]]
        testBeaker3 = [["die1", 3, "unlocked"], ["die2", 4, "unlocked"], ["die3", 5, "unlocked"],
                       ["die4", 6, "unlocked"], ["die5", 1, "unlocked"]]
        sortedBeaker = beaker.dice.sort(beaker.dice[1])
        for die in sortedBeaker.dice:
            die[2] = "unlocked"
        if testBeaker1 == sortedBeaker:
            return True
        elif testBeaker2 == sortedBeaker:
            return True
        elif testBeaker3 == sortedBeaker:
            return True
        else:
            return False

    def computeFull(self, beaker):
        sortedBeaker = beaker.sort(beaker.dice[1])
        return sortedBeaker.dice[0][1] == sortedBeaker.dice[1][1] and sortedBeaker.dice[1][1] == \
               sortedBeaker.dice[2][1] and sortedBeaker.dice[3][1] == \
               sortedBeaker.dice[4][1] and sortedBeaker.dice[0][1] != sortedBeaker.dice[4][1] or \
               sortedBeaker.dice[0][1] == sortedBeaker.dice[1][1] and \
               sortedBeaker.dice[2][1] == sortedBeaker.dice[3][1] and sortedBeaker.dice[3][1] == \
               sortedBeaker.dice[4][1] and sortedBeaker.dice[0][1] != \
               sortedBeaker.dice[4][1]

    def computePoker(self, beaker):
        res = False
        dice = [1, 2, 3, 4, 5, 6]
        for i in dice:
            count = 0
            for die in beaker:
                if (dice[i] == beaker.dice[die][1]):
                    count += 1
                    if (count == 4):
                        return True
        return False

    def computeFiveEqual(self, beaker):
        beakonToSet = set()
        for die in beaker.dice:
            beakonToSet.add(die)
        return beakonToSet.__sizeof__() == 1