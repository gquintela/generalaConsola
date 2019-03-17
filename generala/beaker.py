from random import randint


class Beaker:

    def __init__(self):
        self.dice = [["die1", 0, "unlocked"], ["die2", 0, "unlocked"], ["die3", 0, "unlocked"],
                    ["die4", 0, "unlocked"], ["die5", 0, "unlocked"]]

    def throw_beaker(self):
        for i in range(5):
            if (self.dice[i][2] == "unlocked"):
                self.dice[i][1] = randint(1, 6)

    def print_Beaker(self):
        for i in range(5):
            if (self.dice[i][2] == "locked"):
                print("Die %s: %s (locked)" % (i + 1, self.dice[i][1]))
            elif (self.dice[i][2] == "unlocked"):
                print("Die %s: %s" % (i + 1, self.dice[i][1]))
        print("")

    def dice_to_set(self, dice_in_string):
        res = []
        for s in dice_in_string:
            if(s != ','):
                res.append(s)
        return res

    def lock_dice(self, dice):
        dice_in_set = self.dice_to_set(dice)
        for die in dice_in_set:
            self.dice[int(die) - 1][2] = "locked"
        print(dice_in_set)

    def unlock_dice(self, dice):
        dice_in_set = self.dice_to_set(dice)
        for die in dice_in_set:
            self.dice[int(die) - 1][2] = "unlocked"
        print(dice_in_set)
