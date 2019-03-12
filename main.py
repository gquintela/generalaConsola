from generala import *
from jugador import *
from tablaPuntaje import *

def imprimirPuntos(jugador, cat):
    if (jugador._categorias[cat][2]=="vacio"):       #como puedo hacer para que quede mas declarativo?
        print ("     ")
    elif (jugador._categorias[cat][2]=="tachado"):
        print ("   xXx   ")
    else:
        print("    ",end="")
        print (jugador._categorias[cat][1])


def imprimirTablaPuntaje (jugador):
    print( jugador._nombre )
    print("       UNO:    ",end="")
    imprimirPuntos(jugador,0)
    print("       DOS:    ",end="")
    imprimirPuntos(jugador,1)
    print("       TRES:   ",end="")
    imprimirPuntos(jugador,2)
    print("      CUATRO:  ",end="")
    imprimirPuntos(jugador,3)
    print("      CINCO:   ",end="")
    imprimirPuntos(jugador,4)
    print("      SEIS:    ",end="")
    imprimirPuntos(jugador,5)
    print("     ESCALERA: ",end="")
    imprimirPuntos(jugador,6)
    print("      FULL:    ",end="")
    imprimirPuntos(jugador,7)
    print("     POKER:    ",end="")
    imprimirPuntos(jugador,8)
    print("    GENERALA:  ",end="")
    imprimirPuntos(jugador,9)
    print("GENERALA DOBLE:",end="")
    imprimirPuntos(jugador,10)
    print ("-----------------")
    print("PUNTAJE TOTAL: ",end="")
    print (jugador._puntajeTotal)




###############################################################
###############################################################

print ("Generala para una persona\n\n")

juego=Generala()
jugador01=Jugador()

jugador01._nombre = input("ingrese su nombre:")

imprimirTablaPuntaje(jugador01)







#print ( gon._categorias._uno)
#print (juego.getFinJuego() )
#juego.setFinJuego()
#print (juego.getFinJuego() )



