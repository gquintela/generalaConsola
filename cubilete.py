from random import randint

class Cubilete:
  _dado1=[0,"sin anclar"]
  _dado2=[0,"sin anclar"]
  _dado3=[0,"sin anclar"]
  _dado4=[0,"sin anclar"]
  _dado5=[0,"sin anclar"]

  def tirarCubilete(self):
    pass

  def mostrarValores(self):
    return self._valor
  
  def imprimirCubilete(self):
    print ("Dado 1: %s" % self._dado1 )
    print ("Dado 2: %s" % self._dado2 )
    print ("Dado 3: %s" % self._dado3 )
    print ("Dado 4: %s" % self._dado4 )
    print ("Dado 5: %s" % self._dado5 )
