from generala.beaker import *
from generala.game import *
from generala.player import *


def printPoints(player, cat):
    if (player.categories[cat][1] == "empty"):  # como puedo hacer para que quede mas declarativo?
        return ("")
    elif (player.categories[cat][1] == "crossed"):
        return ("X")
    else:
        return (player.categories[cat][0])


def printPointsTable(player):
    print(str("%s" % (player.name)).center(25, '-'))
    print(str("UNO: %s    |" % printPoints(player, "UNO")).rjust(25, ' '))
    print(str("DOS: %s    |" % printPoints(player, "DOS")).rjust(25, ' '))
    print(str("TRES: %s    |" % printPoints(player, "TRES")).rjust(25, ' '))
    print(str("CUATRO: %s    |" % printPoints(player, "CUATRO")).rjust(25, ' '))
    print(str("CINCO: %s    |" % printPoints(player, "CINCO")).rjust(25, ' '))
    print(str("SEIS: %s    |" % printPoints(player, "SEIS")).rjust(25, ' '))
    print(str("ESCALERA: %s    |" % printPoints(player, "ESCALERA")).rjust(25, ' '))
    print(str("FULL: %s    |" % printPoints(player, "FULL")).rjust(25, ' '))
    print(str("POKER: %s    |" % printPoints(player, "POKER")).rjust(25, ' '))
    print(str("GENERALA: %s    |" % printPoints(player, "GENERALA")).rjust(25, ' '))
    print(str("GENERALA DOBLE: %s    |\n" % printPoints(player, "GENERALA DOBLE")).rjust(26, ' '))



###############################################################
###############################################################

print("Generala for one person\n\n")

game = Game()
player01 = Player()
beaker = Beaker()

player01.name = input("Write your name:")

printPointsTable(player01)

while (game.roundEnded != 2):
    game.throwNumber = 1
    fold = 0
    lockedDices = set()

    beaker.throwBeaker()

    while (game.throwNumber < 3 or fold == 0):

        beaker.printBeaker()
        option = 0

        print("Choose an option:\n")
        print("1) Lock dices.")
        print("2) Unlock dices.")
        print("3) Roll again.")
        print("4) Fold. ")
        print("5) Show the dices. ")
        print("6) Show score. ")

        option = int(input(""))

        if (option == 1):
            dicesToLock = set()
            dicesToLock.add(input(
                'Write the dice\'s index to lock:\n (separate with \',\' if more than one dice is selected.) '))
            beaker.lockDices(dicesToLock)
        if (option == 2):
            dicesToUnlock = set()
            dicesToUnlock.add(input(
                'Write the dice\'s index to unlock:\n (separate with \',\' if more than one dice is selected.) '))
            beaker.unlockDices(dicesToUnlock)
        elif (option == 3):
            beaker.throwBeaker()
            game.throwNumber += 1
            break
        elif (option == 4):
            fold = 1
            break  # plantarse
        elif (option == 5):
            break
        elif (option == 6):  # imprimir tabla de puntos
            printPointsTable(player01)

    print("\n\n\n")
    print("-------------------------------------------------------")
    print("-------------------------------------------------------")
    print("\n")

    printPointsTable(player01)
    beaker.printBeaker()
    print ("What do you want to do?")
    opcion2=input("blablabla")
    game.roundEnded = game.roundEnded + 1
