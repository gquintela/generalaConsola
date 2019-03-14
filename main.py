from cubilete import *
from generala import *
from jugador import *


def imprimirPuntos(jugador, cat):
    if (jugador._categorias[cat][1] == "vacio"):  # como puedo hacer para que quede mas declarativo?
        return ("")
    elif (jugador._categorias[cat][1] == "tachado"):
        return ("X")
    else:
        return (jugador._categorias[cat][0])


def imprimirTablaPuntaje(jugador):
    print(str("%s" % (jugador._nombre)).center(25, '-'))
    print(str("UNO: %s    |" % imprimirPuntos(jugador, "UNO")).rjust(25, ' '))
    print(str("DOS: %s    |" % imprimirPuntos(jugador, "DOS")).rjust(25, ' '))
    print(str("TRES: %s    |" % imprimirPuntos(jugador, "TRES")).rjust(25, ' '))
    print(str("CUATRO: %s    |" % imprimirPuntos(jugador, "CUATRO")).rjust(25, ' '))
    print(str("CINCO: %s    |" % imprimirPuntos(jugador, "CINCO")).rjust(25, ' '))
    print(str("SEIS: %s    |" % imprimirPuntos(jugador, "SEIS")).rjust(25, ' '))
    print(str("ESCALERA: %s    |" % imprimirPuntos(jugador, "ESCALERA")).rjust(25, ' '))
    print(str("FULL: %s    |" % imprimirPuntos(jugador, "FULL")).rjust(25, ' '))
    print(str("POKER: %s    |" % imprimirPuntos(jugador, "POKER")).rjust(25, ' '))
    print(str("GENERALA: %s    |" % imprimirPuntos(jugador, "GENERALA")).rjust(25, ' '))
    print(str("GENERALA DOBLE: %s    |" % imprimirPuntos(jugador, "GENERALA DOBLE")).rjust(25, ' '))

    print("\n\n")


###############################################################
###############################################################

print("Generala para una persona\n\n")

partida = Generala()
jugador01 = Jugador()
cubilete = Cubilete()

jugador01._nombre = input("ingrese su nombre:")

imprimirTablaPuntaje(jugador01)

while (partida._vueltaTerminada != 2):
    tirada = 1
    plantarse = 0
    dadosAnclados = set()

    while (tirada < 3 or plantarse == 0):

        cubilete.tirarCubilete()
        cubilete.imprimirCubilete()
        tirada += 1
        opcion = 0

        print("Que desea hacer?\n")
        print("1) Anclar dados.")
        print("2) Volver a tirar.")
        print("3) Plantarse. ")
        print("4) Mostrar dados. ")
        print("5) Mostrar tabla de puntuacion. ")

        opcion = int(input(""))

        if (opcion == 1):  # anclar dados
            seguirAnclando = 1

            while (seguirAnclando != 2):
                dadoParaAnclar = (input("Ingrese numero de dado a anclar: "))
                cubilete.anclarDado(dadoParaAnclar)
                print("\nDesea anclar mas dados?\n")
                cubilete.imprimirCubilete()
                print("1) Seguir anclando.")
                print("2) No anclar mas.\n")
                seguirAnclando = int(input(""))
        elif (opcion == 2):
            tirada+=1
            break
        elif (opcion == 3):
            plantarse=1
            break  # plantarse
        elif (opcion == 4):
            break
        elif (opcion == 5):  # imprimir tabla de puntos
            imprimirTablaPuntaje(jugador01)

    partida._vueltaTerminada = partida._vueltaTerminada + 1
