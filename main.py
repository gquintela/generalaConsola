from generala import *
from jugador import *
from tablaPuntaje import *


def imprimirTablaPuntaje (jugador):
    print( jugador._nombre )
    print("       UNO:    ")
    print("       DOS:    ")
    print("       TRES:   ")
    print("      CUATRO:  ")
    print("      CINCO:   ")
    print("      SEIS:    ")
    print("     ESCALERA: ")
    print("      FULL:    ")
    print("     POKER:    ")
    print("    GENERALA:  ")
    print("GENERALA DOBLE:")

    if (jugador._categorias._uno[1]=="vacio"):
        print ("     ")
    elif (jugador._categorias._uno[1]=="tachado"):
        print ("   xXx   ")
    else:
        print (jugador._categorias._uno[0])


print ("Generala para una persona\n\n")

juego=Generala()
jugador01=Jugador()

jugador01._nombre = input("ingrese su nombre:")

imprimirTablaPuntaje(jugador01)







#print ( gon._categorias._uno)
#print (juego.getFinJuego() )
#juego.setFinJuego()
#print (juego.getFinJuego() )



