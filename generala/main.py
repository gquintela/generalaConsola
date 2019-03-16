from generala.beaker import Beaker
from generala.game import Game
from generala.player import Player

###############################################################
###############################################################

print("Generala for one person\n\n")

game = Game()
player01 = Player()
beaker = Beaker()

player01.name = input("Write your name:")

player01.print_points_table()

while (game.round != 2):
    game.throw_number = 1
    fold = 0
    locked_dice = set()

    beaker.throw_beaker()
    beaker.print_Beaker()

    while (game.throw_number < 3 and fold == 0):

        option = 0

        print("Choose an option:\n")
        print("1) Lock dice.")
        print("2) Unlock dice.")
        print("3) Roll again.")
        print("4) Fold. ")
        print("5) Show the dice. ")
        print("6) Show score. ")

        option = int(input(""))

        if (option == 1):
            dice_to_lock=(input(
                'Write the die\'s index to lock:\n (separate with \',\' if more than one die is selected.) '))
            beaker.lock_dice(dice_to_lock)
        elif (option == 2):
            dice_to_unlock=(input(
                'Write the die\'s index to unlock:\n (separate with \',\' if more than one die is selected.) '))
            beaker.unlock_dice(dice_to_unlock)
        elif (option == 3):
            beaker.throw_beaker()
            game.throw_number += 1
        elif (option == 4):
            fold = 1
        elif (option == 5):
            beaker.print_Beaker()
        elif (option == 6):  # imprimir tabla de puntos
            player01.print_points_table(player01)

    print("\n\n\n")
    print("-------------------------------------------------------")
    print("-------------------------------------------------------")
    print("\n")

    player01.print_points_table(player01)
    beaker.print_Beaker()
    print ("What do you want to do?")
    opcion2=input("blablabla")
    game.round = game.round + 1
