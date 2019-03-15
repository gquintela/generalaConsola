from random import randint


class Beaker:
    def __init__(self):
        self.dice = [["die1", 0, "unlocked"], ["die2", 0, "unlocked"], ["die3", 0, "unlocked"],
                      ["die4", 0, "unlocked"], ["die5", 0, "unlocked"]]

    def throwBeaker(self):
        for i in range(5):
            if (self.dice[i][2] == "unlocked"):
                self.dice[i][1] = randint(1, 6)

    def printBeaker(self):
        for i in range(5):
            if (self.dice[i][2] == "locked"):
                print("Die %s: %s (locked)" % (i + 1, self.dice[i][1]))
            elif (self.dice[i][2] == "unlocked"):
                print("Die %s: %s" % (i + 1, self.dice[i][1]))
        print("")

    def diceToSet(diceInString):
        res=[]
        for s in diceInString:
            if(s!=','):
                res.append(s)
        return res

    #TODO: lockDice and unlockDice break when input is more than one integer (i.e. '1,2')
    def lockDice(self, dice):
        diceInSet = self.diceToSet(dice)
        for die in diceInSet:
            self.dice[int(die) - 1][2] = "locked"

    def unlockDice(self, dice):
        for die in dice:
            self.dice[int(die) - 1][2] = "unlocked"