from generala.prompts import Prompts

class Game:

    def __init__(self):
        self.round = 0
        self.throw_number = 0
        self.prompts = Prompts()

    def number_count(self, beaker, number):
        count = 0
        for die in range(5):
            if beaker.dice[die][1] == number:
                count += beaker.dice[die][1]
        return count

    def compute_stairway(self, beaker):
        if(self.throw_number is 1):
            first_throw = 5
        else :
            first_throw = 0

        test_beaker_01 = [1,2,3,4,5]
        test_beaker_02 = [2,3,4,5,6]
        test_beaker_03 = [3,4,5,6,1]

        sorted_beaker = []
        for i in range(5):
            sorted_beaker.append(beaker.dice[i][1])

        if test_beaker_01 == sorted_beaker:
            return 20 + first_throw
        elif test_beaker_02 == sorted_beaker:
            return 20 + first_throw
        elif test_beaker_03 == sorted_beaker:
            return 20 + first_throw
        else:
            return 0

    def compute_fullhouse(self, beaker):
        if (self.throw_number is 1):
            first_throw = 5
        else:
            first_throw = 0
        sorted_beaker = []
        for i in range(5):
            sorted_beaker.append(beaker.dice[i][1])
        sorted_beaker.sort()
        predicate =  sorted_beaker[0] == sorted_beaker[1] and sorted_beaker[1] == \
               sorted_beaker[2] and sorted_beaker[3] == \
               sorted_beaker[4] and sorted_beaker[0] != sorted_beaker[4] or \
               sorted_beaker[0] == sorted_beaker[1] and \
               sorted_beaker[2] == sorted_beaker[3] and sorted_beaker[3] == \
               sorted_beaker[4] and sorted_beaker[0] != \
               sorted_beaker[4]
        if (predicate):
            return 30 + first_throw
        else:
            return 0

    def compute_poker(self, beaker):
        if (self.throw_number is 1):
            first_throw = 5
        else:
            first_throw = 0
        dice = [1, 2, 3, 4, 5, 6]
        for i in dice:
            count = 0
            for die in beaker:
                if (dice[i] == beaker.dice[die][1]):
                    count += 1
                    if (count == 4):
                        return 40 + first_throw
        return 0

    def compute_five_equal(self, beaker):
        if (self.throw_number is 1):
            first_throw = 50
        else:
            first_throw = 0

        beaker_to_set = set()
        for die in beaker.dice:
            beaker_to_set.add(die[1])
        if(beaker_to_set.__sizeof__() == 1):
            return 50 +first_throw
        else:
            return 0

    def compmute_posibilities(self,player,beaker):
        posible_results = []
        #one
        if(player.categories["one"] is None):
            posible_results.append(("one",self.number_count(beaker,1)))
        if(player.categories["two"] is None):
            posible_results.append(("two", self.number_count(beaker, 2)))
        if(player.categories["three"] is None):
            posible_results.append(("three", self.number_count(beaker, 3)))
        if(player.categories["four"] is None):
            posible_results.append(("four", self.number_count(beaker, 4)))
        if(player.categories["five"] is None):
            posible_results.append(("five", self.number_count(beaker, 5)))
        if(player.categories["six"] is None):
            posible_results.append(("six", self.number_count(beaker, 6)))
        if(player.categories["stairway"] is None): #TODO: test!it doesnt work!!!
            posible_results.append(("stairway",self.compute_stairway(beaker)))
        if(player.categories["fullhouse"] is None):
            posible_results.append(("fullhouse", self.compute_fullhouse(beaker)))
        if(player.categories["generala"] is None):
            posible_results.append(("generala", self.compute_five_equal(beaker)))
        if(player.categories["double_generala"] != None and int(player.categories["generala"]) > 0  ):
            posible_results.append(("double_generala", self.compute_stairway(beaker))+500)
        elif(player.categories["double_generala"] == None):
            posible_results.append(("double_generala", 0))
        return posible_results
