from generala.beaker import Beaker
from generala.judge import Judge
from generala.player import Player
from generala.prompts import Prompts


def clear_screen():
    for i in range(50):
        print("\n")


class Game:

    def __init__(self):
        self.judge = Judge()
        self.round = 1
        self.throw_number = 1
        self.players = []
        self.beaker = Beaker()
        self.prompts = Prompts()

    def add_player(self, player):
        new_player = Player()
        new_player.name = player
        self.players.append(new_player)

#######################################################################

    def play_game(self):
        print(self.prompts.dic["welcome"] + "\n")
        print(self.prompts.dic["players_number"] + "\n")

        player_number = input()
        while (not str(player_number).isnumeric()) or int(player_number) < 1 or int(player_number) > 4:
            print(self.prompts.dic["error_player_number"] + "\n")
            print(self.prompts.dic["players_number"] + "\n")
            player_number = input()

        for i in range(int(player_number)):
            print("%s %d: " % (self.prompts.dic["new_name"], i + 1))
            new_player = input()
            self.add_player(new_player)

        clear_screen()

        while self.round != 12:
            for player in self.players:
                player.print_points_table()
                self.throw_number = 1
                print("")
                fold = 0
                locked_dice = set()

                self.beaker.throw_beaker()


                while self.throw_number < 3 and fold == 0:
                    clear_screen()
                    player.print_points_table()
                    self.beaker.print_Beaker()

                    option = 0
                    print(player.name + self.prompts.dic["has_to_play"])
                    print(self.prompts.dic["throw_number"] + str(self.throw_number))

                    print(self.prompts.dic["choose_option"] + "\n")
                    print("1) " + self.prompts.dic["lock_dice"])
                    print("2) " + self.prompts.dic["unlock_dice"])
                    print("3) " + self.prompts.dic["roll_again"])
                    print("4) " + self.prompts.dic["fold"])
                    print("5) " + self.prompts.dic["show_dice"])
                    print("6) " + self.prompts.dic["show_score"])
                    print("7) " + self.prompts.dic["sort_dice"])
                    print ("")
                    print(self.prompts.dic["choose"])

                    option = input()
                    while (not option.isnumeric()) or int(option) < 1 or int(option) > 7:
                        print(self.prompts.dic["error_option"] + "\n")
                        option = input()

                    option = int(option)
                    if option == 1:
                        dice_to_lock = (input(self.prompts.dic["lock_prompt"]))
                        self.beaker.lock_dice(dice_to_lock)
                        self.beaker.print_Beaker()
                    elif option == 2:
                        dice_to_unlock = (input(self.prompts.dic["unlock_prompt"]))
                        self.beaker.unlock_dice(dice_to_unlock)
                        self.beaker.print_Beaker()
                    elif option == 3:
                        self.beaker.throw_beaker()
                        self.throw_number += 1
                        self.beaker.print_Beaker()
                    elif option == 4:
                        fold = 1
                    elif option == 5:
                        self.beaker.print_Beaker()
                    elif option == 6:  # imprimir tabla de puntos
                        player.print_points_table()
                    elif option == 7:
                        self.beaker.sort()
                        self.beaker.print_Beaker()



                print("\n\n\n")
                print("-------------------------------------------------------")
                print("-------------------------------------------------------")
                print("\n")

                self.beaker.unlock_dice([1, 2, 3, 4, 5])
                player.print_points_table()
                self.beaker.print_Beaker()
                posibilities = self.judge.compmute_posibilities(self, player)
                print(self.prompts.dic["choose_points"] + "\n")
                self.judge.print_posibilities(posibilities)

                option2 = input()
                while (not option2.isnumeric()) or int(option2) < 1 or int(option2) > posibilities.__len__() :
                    print(self.prompts.dic["error_choose_points"] + "\n")
                    option2 = input()

                category_to_write = posibilities[int(option2)-1][0]
                amount = posibilities[int(option2)-1][1]

                self.judge.write_score(player, category_to_write, amount)
            self.round += 1

        self.judge.print_final_results(self)
