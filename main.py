from beaker import *
from game import *
from player import *


def printPoints(player, cat):
    if (player._categories[cat][1] == "empty"):  # como puedo hacer para que quede mas declarativo?
        return ("")
    elif (player._categories[cat][1] == "crossed"):
        return ("X")
    else:
        return (player._categories[cat][0])


def printPointsTable(player):
    print(str("%s" % (player._name)).center(25, '-'))
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
    print(str("GENERALA DOBLE: %s    |" % printPoints(player, "GENERALA DOBLE")).rjust(25, ' '))

    print("\n\n")


###############################################################
###############################################################

print("Generala for one person\n\n")

game = Game()
player01 = Player()
beaker = Beaker()

player01._name = input("Write your name:")

printPointsTable(player01)

while (game._roundEnded != 2):
    player01._throwNumber = 1
    fold = 0
    lockedDices = set()

    while (player01._throwNumber < 3 or fold == 0):

        beaker.throwBeaker()
        beaker.printBeaker()
        player01._throwNumber += 1
        option = 0

        print("Choose an option:\n")
        print("1) Lock dices.")
        print("2) Roll again.")
        print("3) Fold. ")
        print("4) Show the dices. ")
        print("5) Show score. ")

        option = int(input(""))

        if (option == 1):  # anclar dados
            keepLocking = 1

            while (keepLocking != 2):
                diceToLock = (input("Write the dice's index to lock: "))
                beaker.lockDice(diceToLock)
                print("\nDo you wish to lock more dices?\n")
                beaker.printBeaker()
                print("1) Keep locking.")
                print("2) No, thanks.\n")
                keepLocking = int(input(""))
        elif (option == 2):
            player01._throwNumber += 1
            break
        elif (option == 3):
            fold=1
            break  # plantarse
        elif (option == 4):
            break
        elif (option == 5):  # imprimir tabla de puntos
            printPointsTable(player01)

    game._roundEnded = game._roundEnded + 1
