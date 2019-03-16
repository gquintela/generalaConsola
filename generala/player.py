class Player:
    def __init__(self):
        self.name = ""
        self.totalPoints = 0
        self.categories = {  #empty/crossed/filled
            "UNO": (0, "empty"),
            "DOS": (0, "empty"),
            "TRES": (0, "empty"),
            "CUATRO": (0, "empty"),
            "CINCO": (0, "empty"),
            "SEIS": (0, "empty"),
            "ESCALERA": (0, "empty"),
            "FULL": (0, "empty"),
            "POKER": (0, "empty"),
            "GENERALA": (0, "empty"),
            "GENERALA DOBLE": (0, "empty")
        }

    def printPoints(self, cat):
        if (self.categories[cat][1] == "empty"):  # como puedo hacer para que quede mas declarativo?
            return ("")
        elif (self.categories[cat][1] == "crossed"):
            return ("X")
        else:
            return (self.categories[cat][0])


    def printPointsTable(self):
        print(str("%s" % (self.name)).center(25, '-'))
        print(str("UNO: %s    |" % self.printPoints("UNO")).rjust(25, ' '))
        print(str("DOS: %s    |" % self.printPoints("DOS")).rjust(25, ' '))
        print(str("TRES: %s    |" % self.printPoints("TRES")).rjust(25, ' '))
        print(str("CUATRO: %s    |" % self.printPoints("CUATRO")).rjust(25, ' '))
        print(str("CINCO: %s    |" % self.printPoints("CINCO")).rjust(25, ' '))
        print(str("SEIS: %s    |" % self.printPoints("SEIS")).rjust(25, ' '))
        print(str("ESCALERA: %s    |" % self.printPoints("ESCALERA")).rjust(25, ' '))
        print(str("FULL: %s    |" % self.printPoints("FULL")).rjust(25, ' '))
        print(str("POKER: %s    |" % self.printPoints("POKER")).rjust(25, ' '))
        print(str("GENERALA: %s    |" % self.printPoints("GENERALA")).rjust(25, ' '))
        print(str("GENERALA DOBLE: %s    |\n" % self.printPoints("GENERALA DOBLE")).rjust(26, ' '))

    def writeResult(self):
        for category in self.categories:
            if self.categories["UNO"][1]=="empty":
                pass