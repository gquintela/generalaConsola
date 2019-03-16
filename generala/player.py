class Player:

    def __init__(self):
        self.name = ""
        self.total_points = 0
        self.categories = {
            "UNO": (None),
            "DOS": (None),
            "TRES": (None),
            "CUATRO": (None),
            "CINCO": (None),
            "SEIS": (None),
            "ESCALERA": (None),
            "FULL": (None),
            "POKER": (None),
            "GENERALA": (None),
            "GENERALA DOBLE": (None)
        }

    def print_points(self, cat):
        if (self.categories[cat] == None):  # como puedo hacer para que quede mas declarativo?
            return ("")
        elif (self.categories[cat] == 0):
            return ("X")
        else:
            return (self.categories[cat])


    def print_points_table(self):
        print(str("%s" % (self.name)).center(25, '-'))
        print(str("UNO: %s    |" % self.print_points("UNO")).rjust(25, ' '))
        print(str("DOS: %s    |" % self.print_points("DOS")).rjust(25, ' '))
        print(str("TRES: %s    |" % self.print_points("TRES")).rjust(25, ' '))
        print(str("CUATRO: %s    |" % self.print_points("CUATRO")).rjust(25, ' '))
        print(str("CINCO: %s    |" % self.print_points("CINCO")).rjust(25, ' '))
        print(str("SEIS: %s    |" % self.print_points("SEIS")).rjust(25, ' '))
        print(str("ESCALERA: %s    |" % self.print_points("ESCALERA")).rjust(25, ' '))
        print(str("FULL: %s    |" % self.print_points("FULL")).rjust(25, ' '))
        print(str("POKER: %s    |" % self.print_points("POKER")).rjust(25, ' '))
        print(str("GENERALA: %s    |" % self.print_points("GENERALA")).rjust(25, ' '))
        print(str("GENERALA DOBLE: %s    |\n" % self.print_points("GENERALA DOBLE")).rjust(26, ' '))