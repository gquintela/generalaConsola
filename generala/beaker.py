from random import randint
from generala.die import Die


class Beaker:

    def __init__(self):
        self.dice = [Die() for i in range(5)]

    def __eq__(self, other):
        return self.dice == other.dice

    def throw_beaker(self):
        for i in range(5):
            if (self.dice[i].status == False):
                self.dice[i].value = randint(1, 6)

    def print_Beaker(self):
        for i in range(5):
            if (self.dice[i].status == True):
                print("Die %s: %s (locked)" % (i + 1, self.dice[i].value))
            elif (self.dice[i].status == False):
                print("Die %s: %s" % (i + 1, self.dice[i].value))
        print("")

    def dice_to_set(self, dice_in_string):
        res = []
        for s in dice_in_string:
            if (s != ','):
                res.append(s)
        return res

    def lock_dice(self, dice):
        dice_in_set = self.dice_to_set(dice)
        for die in dice_in_set:
            self.dice[int(die) - 1].status = True

    def unlock_dice(self, dice):
        dice_in_set = self.dice_to_set(dice)
        for die in dice_in_set:
            self.dice[int(die) - 1].status = False

    def sort(self):
        self.dice.sort(key=lambda die: die.value)

    def custom_beaker(self,int0,int1,int2,int3,int4):
        self.dice[0].value = int0
        self.dice[1].value = int1
        self.dice[2].value = int2
        self.dice[3].value = int3
        self.dice[4].value = int4
        self.dice[0].status = False
        self.dice[1].status = False
        self.dice[2].status = False
        self.dice[3].status = False
        self.dice[4].status = False