from generala.beaker import Beaker
from generala.rules import Rules
from generala.player import Player
from generala.game import Game

###############################################################
###############################################################

game = Game()

print(game.prompts.dic["welcome"] + "\n")

print(game.prompts.dic["players_number"] + "\n")

player_number = input()

for i in range(int(player_number)):
    print(game.prompts.dic["new_name"],i+1)
    new_player = input()
    game.add_player(new_player)


while (game.round != 11):
    for player_index in range(game.players.__sizeof__()):
        game.players[player_index].print_points_table()
        game.throw_number = 1
        print("")
        fold = 0
        locked_dice = set()

        game.beaker.throw_beaker()
        game.beaker.print_Beaker()

        while (game.throw_number < 3 and fold == 0):

            option = 0
            print("round: ", game.throw_number)

            print(game.prompts.dic["choose_option"] + "\n")
            print("1) " + game.prompts.dic["lock_dice"])
            print("2) " + game.prompts.dic["unlock_dice"])
            print("3) " + game.prompts.dic["roll_again"])
            print("4) " + game.prompts.dic["fold"])
            print("5) " + game.prompts.dic["show_dice"])
            print("6) " + game.prompts.dic["show_score"])
            print("7) " + game.prompts.dic["sort_dice"])

            option = int(input(""))

            if (option == 1):
                dice_to_lock = (input(game.prompts.dic["lock_prompt"]))
                game.beaker.lock_dice(dice_to_lock)
                game.beaker.print_Beaker()
            elif (option == 2):
                dice_to_unlock = (input(game.prompts.dic["unlock_prompt"]))
                game.beaker.unlock_dice(dice_to_unlock)
                game.beaker.print_Beaker()
            elif (option == 3):
                game.beaker.throw_beaker()
                game.throw_number += 1
                game.beaker.print_Beaker()
            elif (option == 4):
                fold = 1
            elif (option == 5):
                game.beaker.print_Beaker()
            elif (option == 6):  # imprimir tabla de puntos
                player01.print_points_table(player01)
            elif (option == 7):
                beaker.sort()
                beaker.print_Beaker()

        print("\n\n\n")
        print("-------------------------------------------------------")
        print("-------------------------------------------------------")
        print("\n")

        game.players[player_index].print_points_table()
        game.beaker.print_Beaker()
        posibilities = game.rules.compmute_posibilities(game.players[player_index], game.beaker)
        print(game.rules.prompts.dic["choose_points"]+"\n")
        game.rules.print_posibilities(posibilities)
        opcion2 = input("blablabla")
        game.rules.round = game.rules.round + 1
