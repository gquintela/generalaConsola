from generala.beaker import Beaker
from generala.game import Game
from generala.player import Player


###############################################################
###############################################################

game = Game()

print(game.prompts.dic["welcome"]+"\n")

player01 = Player()
beaker = Beaker()

player01.name = input(game.prompts.dic["new_name"])

player01.print_points_table()

while (game.round != 2):
    game.throw_number = 1
    print("round: ",game.throw_number)
    print("")
    fold = 0
    locked_dice = set()

    beaker.throw_beaker()
    beaker.print_Beaker()

    while (game.throw_number < 3 and fold == 0):

        option = 0

        print(game.prompts.dic["choose_option"]+"\n")
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
            beaker.lock_dice(dice_to_lock)
            beaker.print_Beaker()
        elif (option == 2):
            dice_to_unlock = (input(game.prompts.dic["unlock_prompt"]))
            beaker.unlock_dice(dice_to_unlock)
            beaker.print_Beaker()
        elif (option == 3):
            beaker.throw_beaker()
            game.throw_number += 1
            beaker.print_Beaker()
        elif (option == 4):
            fold = 1
        elif (option == 5):
            beaker.print_Beaker()
        elif (option == 6):  # imprimir tabla de puntos
            player01.print_points_table(player01)
        elif (option == 7):
            beaker.sort()
            beaker.print_Beaker()

    print("\n\n\n")
    print("-------------------------------------------------------")
    print("-------------------------------------------------------")
    print("\n")

    player01.print_points_table()
    beaker.print_Beaker()
    posibilities = game.compmute_posibilities(player01,beaker)
    print (posibilities)
    print(game.prompts.dic["choose_points"])
    opcion2 = input("blablabla")
    game.round = game.round + 1
