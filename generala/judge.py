from generala.beaker import Beaker


class Judge:

    def number_count(self, game, number):
        count = 0
        for die in range(5):
            if game.beaker.dice[die].value == number:
                count += game.beaker.dice[die].value
        return count

    def compute_stairway(self, game):
        if (game.throw_number is 1):
            first_throw = 5
        else:
            first_throw = 0

        test_beaker_01 = Beaker()
        test_beaker_02 = Beaker()
        test_beaker_03 = Beaker()

        test_beaker_01.custom_beaker(1, 2, 3, 4, 5)
        test_beaker_02.custom_beaker(2, 3, 4, 5, 6)
        test_beaker_03.custom_beaker(1, 3, 4, 5, 6)

        sorted_beaker = game.beaker
        sorted_beaker.sort()
        sorted_beaker.unlock_dice([1, 2, 3, 4, 5])

        if test_beaker_01 == sorted_beaker:
            return 20 + first_throw
        elif test_beaker_02 == sorted_beaker:
            return 20 + first_throw
        elif test_beaker_03 == sorted_beaker:
            return 20 + first_throw
        else:
            return 0

    def compute_fullhouse(self, game):
        if (game.throw_number is 1):
            first_throw = 5
        else:
            first_throw = 0
        sorted_beaker = []
        for i in range(5):
            sorted_beaker.append(game.beaker.dice[i].value)
        sorted_beaker.sort()
        predicate = sorted_beaker[0] == sorted_beaker[1] and sorted_beaker[1] == \
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

    def compute_poker(self, game):
        if (game.throw_number is 1):
            first_throw = 5
        else:
            first_throw = 0

        for i in range(6):
            count = 0
            for die in game.beaker.dice:
                if (i + 1 == die.value):
                    count += 1
                    if (count == 4):
                        return 40 + first_throw
        return 0

    def compute_five_equal(self, game):
        if (game.throw_number is 1):
            first_throw = 50
        else:
            first_throw = 0

        beaker_to_set = set()
        for die in game.beaker.dice:
            beaker_to_set.add(die.value)
        if (beaker_to_set.__sizeof__() == 1):
            return 50 + first_throw
        else:
            return 0

    def compmute_posibilities(self, game, player):
        possible_results = []
        # one
        if player.categories["one"] is None:
            possible_results.append(("one", self.number_count(game, 1)))
        if player.categories["two"] is None:
            possible_results.append(("two", self.number_count(game, 2)))
        if player.categories["three"] is None:
            possible_results.append(("three", self.number_count(game, 3)))
        if player.categories["four"] is None:
            possible_results.append(("four", self.number_count(game, 4)))
        if player.categories["five"] is None:
            possible_results.append(("five", self.number_count(game, 5)))
        if player.categories["six"] is None:
            possible_results.append(("six", self.number_count(game, 6)))
        if player.categories["stairway"] is None:
            possible_results.append(("stairway", self.compute_stairway(game)))
        if player.categories["fullhouse"] is None:
            possible_results.append(("fullhouse", self.compute_fullhouse(game)))
        if player.categories["poker"] is None:
            possible_results.append(("poker", self.compute_poker(game)))
        if player.categories["generala"] is None:
            possible_results.append(("generala", self.compute_five_equal(game)))
        if player.categories["double_generala"] != None and int(player.categories["generala"]) > 0:
            possible_results.append(("double_generala", self.compute_five_equal(game)) + 500)
        elif player.categories["double_generala"] == None:
            possible_results.append(("double_generala", 0))
        return possible_results

    def print_posibilities(self, posible_results):
        for i in range(len(posible_results)):
            print("%i) %s: %i points" % (int(i + 1), posible_results[i][0], int(posible_results[i][1])))

    def write_score(self, player, category, amount):
        player.categories[category] = amount
        player.score += amount

    def print_final_results(self, game):
        print(game.prompts.dic["final_results"] + "\n")
        winners = []
        winners_score = 0
        for player in game.players:
            player.print_points_table()
            print("")
            if player.score > winners_score:
                winners_score = player.score
                winners.clear()
                winners.append(player)
            elif player.score == winners_score:
                winners.append(player)

        if len(game.players) is 1 and len(winners) is 1:
            print(game.prompts.dic["one_player_game"] + "\n")
        elif len(winners) is 1:
            print(game.prompts.dic["one_winner"] + "\n")
            print("%s with %i points!" % (winners[0].name, winners[0].score))
        else:
            print(game.prompts.dic["tie"])
            for winner in winners:
                print("%s" % winner.name)
            print("\n with %i points!" % winner.score)
