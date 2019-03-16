class Player:

    def __init__(self):
        self.name = ""
        self.total_points = 0
        self.categories = {
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

    def print_points(self, cat):
        if (self.categories[cat][1] == "empty"):  # como puedo hacer para que quede mas declarativo?
            return ("")
        elif (self.categories[cat][1] == "crossed"):
            return ("X")
        else:
            return (self.categories[cat][0])


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