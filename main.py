
from cubilete import *
from generala import *
from jugador import *


def imprimirPuntos(jugador, cat):
    if (jugador._categorias[cat][1] == "vacio"):  # como puedo hacer para que quede mas declarativo?
        return ("")
    elif (jugador._categorias[cat][1] == "tachado"):
        return("X")
    else:
        return(jugador._categorias[cat][0])


def imprimirTablaPuntaje(jugador):
    print( str("%s" % (jugador._nombre)).center(25,'-') )
    print ( str("UNO: %s    |" % imprimirPuntos(jugador, "UNO") ).rjust(25,' ') )
    print(str("DOS: %s    |"% imprimirPuntos(jugador, "DOS")).rjust(25, ' '))
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

while (partida._vueltaTerminada != 11):
    tirada=1
    plantarse=0
    dadosAnclados=set()

    while (tirada<3 or plantarse==1):
    
      cubilete.tirarCubilete()
   #   print (cubilete.imprimirCubilete() )
      tirada+=1
      opcion=0
      

      print("Que desea hacer?\n")
      print("1) Anclar dados.")
      print("2) Volver a tirar.")
      print("3) Plantarse. ")

      opcion=int(input(""))

      if (opcion==1): #anclar dados
        seguirAnclando=1

        while(seguirAnclando!=2):
          dadosAnclados.add(input("Ingrese numero de dado a anclar: "))
          print("\nDesea anclar mas dados?\n")
          if (dadosAnclados.__sizeof__()!=0):
              print ("INDICE DE DADOS ANCLADOS: %s\n" % dadosAnclados)
          print("1) Seguir anclando.")
          print("2) No anclar mas.\n")
          seguirAnclando=int(input("")) 
      


      elif (opcion==2):
        pass # tirar dados
      else:
        pass # plantarse


    partida._vueltaTerminada=partida._vueltaTerminada+1
