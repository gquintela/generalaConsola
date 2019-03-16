class Game:

    def __init__(self):
        self.round = 0
        self.throw_number = 0

    def number_count(self, beaker, number):
        count = 0
        for die in beaker:
            if beaker.dice[die][1] == number:
                count += beaker.dice[die][1]
        return count

    def compute_stairway(self, beaker):
        test_beaker_01 = [["die1", 1, "unlocked"], ["die2", 2, "unlocked"], ["die3", 3, "unlocked"],
                          ["die4", 4, "unlocked"], ["die5", 5, "unlocked"]]
        test_beaker_02 = [["die1", 2, "unlocked"], ["die2", 3, "unlocked"], ["die3", 4, "unlocked"],
                          ["die4", 5, "unlocked"], ["die5", 6, "unlocked"]]
        test_beaker_03 = [["die1", 3, "unlocked"], ["die2", 4, "unlocked"], ["die3", 5, "unlocked"],
                          ["die4", 6, "unlocked"], ["die5", 1, "unlocked"]]
        sorted_beaker = beaker.dice.sort(beaker.dice[1])
        for die in sorted_beaker.dice:
            die[2] = "unlocked"
        if test_beaker_01 == sorted_beaker:
            return True
        elif test_beaker_02 == sorted_beaker:
            return True
        elif test_beaker_03 == sorted_beaker:
            return True
        else:
            return False

    def compute_fullhouse(self, beaker):
        sorted_beaker = beaker.sort(beaker.dice[1])
        return sorted_beaker.dice[0][1] == sorted_beaker.dice[1][1] and sorted_beaker.dice[1][1] == \
               sorted_beaker.dice[2][1] and sorted_beaker.dice[3][1] == \
               sorted_beaker.dice[4][1] and sorted_beaker.dice[0][1] != sorted_beaker.dice[4][1] or \
               sorted_beaker.dice[0][1] == sorted_beaker.dice[1][1] and \
               sorted_beaker.dice[2][1] == sorted_beaker.dice[3][1] and sorted_beaker.dice[3][1] == \
               sorted_beaker.dice[4][1] and sorted_beaker.dice[0][1] != \
               sorted_beaker.dice[4][1]

    def compute_poker(self, beaker):
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

    def compute_five_equal(self, beaker):
        beaker_to_set = set()
        for die in beaker.dice:
            beaker_to_set.add(die)
        return beaker_to_set.__sizeof__() == 1