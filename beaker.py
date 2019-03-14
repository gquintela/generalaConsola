from random import randint


class Beaker:
    _dices = [["dice1", 0, "unlocked"], ["dice2", 0, "unlocked"], ["dice3", 0, "unlocked"],
              ["dice4", 0, "unlocked"], ["dice5", 0, "unlocked"]]

    def throwBeaker(self):
        for i in range(5):
            if (self._dices[i][2] == "unlocked"):
                self._dices[i][1] = randint(1, 6)
            elif(self._dices[i][2] == "locked"):
                self._dices[i][2] = "unlocked"

    def printBeaker(self):
        for i in range(5):
            if(self._dices[i][2]== "locked"):
                print("Dice %s: %s (locked)" % (i + 1, self._dices[i][1]))
            else:
                print("Dice %s: %s" % (i + 1, self._dices[i][1]))

    def lockDice(self, dice):
        self._dices[int(dice) - 1][2]= "locked"

