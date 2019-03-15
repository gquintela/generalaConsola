from random import randint


class Beaker:
    def __init__(self):
        self.dices = [["dice1", 0, "unlocked"], ["dice2", 0, "unlocked"], ["dice3", 0, "unlocked"],
                      ["dice4", 0, "unlocked"], ["dice5", 0, "unlocked"]]

    def throwBeaker(self):
        for i in range(5):
            if (self.dices[i][2] == "unlocked"):
                self.dices[i][1] = randint(1, 6)

    def printBeaker(self):
        for i in range(5):
            if (self.dices[i][2] == "locked"):
                print("Dice %s: %s (locked)" % (i + 1, self.dices[i][1]))
            elif (self.dices[i][2] == "unlocked"):
                print("Dice %s: %s" % (i + 1, self.dices[i][1]))
        print("")

    #TODO: lockDices and unlockDices break when input is more than one integer (i.e. '1,2')
    def lockDices(self, dices):
        for dice in dices:
            self.dices[int(dice) - 1][2] = "locked"

    def unlockDices(self, dices):
        for dice in dices:
            self.dices[int(dice) - 1][2] = "unlocked"