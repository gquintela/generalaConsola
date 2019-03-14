from random import randint


class Cubilete:
    _dados = [["dado1", 0, "sin anclar"], ["dado2", 0, "sin anclar"], ["dado3", 0, "sin anclar"],
              ["dado4", 0, "sin anclar"], ["dado5", 0, "sin anclar"]]

    def tirarCubilete(self):
        for i in range(5):
            if (self._dados[i][2] == "sin anclar"):
                self._dados[i][1] = randint(1, 6)
            elif(self._dados[i][2] == "anclado"):
                self._dados[i][2] = "sin anclar"

    def imprimirCubilete(self):
        for i in range(5):
            if(self._dados[i][2]=="anclado"):
                print("Dado %s: %s (anclado)" % (i + 1, self._dados[i][1]))
            else:
                print("Dado %s: %s" % (i + 1, self._dados[i][1]))

    def anclarDado(self,dado):
        self._dados[int(dado)-1][2]="anclado"

