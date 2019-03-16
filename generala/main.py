from generala.beaker import *
from generala.game import *
from generala.player import *

###############################################################
###############################################################

print("Generala for one person\n\n")

game = Game()
player01 = Player()
beaker = Beaker()

player01.name = input("Write your name:")

player01.printPointsTable()

while (game.round != 2):
    game.throwNumber = 1
    fold = 0
    lockedDice = set()

    beaker.throwBeaker()
    beaker.printBeaker()

    while (game.throwNumber < 3 and fold == 0):

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
            diceToLock=(input(
                'Write the die\'s index to lock:\n (separate with \',\' if more than one die is selected.) '))
            beaker.lockDice(diceToLock)
        elif (option == 2):
            diceToUnlock=(input(
                'Write the die\'s index to unlock:\n (separate with \',\' if more than one die is selected.) '))
            beaker.unlockDice(diceToUnlock)
        elif (option == 3):
            beaker.throwBeaker()
            game.throwNumber += 1
        elif (option == 4):
            fold = 1
        elif (option == 5):
            beaker.printBeaker()
        elif (option == 6):  # imprimir tabla de puntos
            player01.printPointsTable(player01)

    print("\n\n\n")
    print("-------------------------------------------------------")
    print("-------------------------------------------------------")
    print("\n")

    player01.printPointsTable(player01)
    beaker.printBeaker()
    print ("What do you want to do?")
    opcion2=input("blablabla")
    game.round = game.round + 1
