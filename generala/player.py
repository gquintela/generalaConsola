from generala.prompts import Prompts
from generala.judge import Judge


class Player():

    def __init__(self):
        self.name = ""
        self.categories = {
            "one": (None),
            "two": (None),
            "three": (None),
            "four": (None),
            "five": (None),
            "six": (None),
            "stairway": (None),
            "fullhouse": (None),
            "poker": (None),
            "generala": (None),
            "double_generala": (None)
        }
        self.score = 0

    def print_points(self, cat):
        if (self.categories[cat] is None):
            return ("")
        elif (self.categories[cat] == 0):
            return ("X")
        else:
            return (self.categories[cat])

    def print_points_table(self):
        print(str("%s" % (self.name)).center(25, '-'))
        # print(str(game.prompts.dic["one"] + ": %s    |" % self.print_points(game.prompts.dic["one"])).rjust(25, ' ')) #

        print(str("one: %s    |" % self.print_points("one")).rjust(25, ' '))
        print(str("two: %s    |" % self.print_points("two")).rjust(25, ' '))
        print(str("three: %s    |" % self.print_points("three")).rjust(25, ' '))
        print(str("four: %s    |" % self.print_points("four")).rjust(25, ' '))
        print(str("five: %s    |" % self.print_points("five")).rjust(25, ' '))
        print(str("six: %s    |" % self.print_points("six")).rjust(25, ' '))
        print(str("stairway: %s    |" % self.print_points("stairway")).rjust(25, ' '))
        print(str("fullhouse: %s    |" % self.print_points("fullhouse")).rjust(25, ' '))
        print(str("poker: %s    |" % self.print_points("poker")).rjust(25, ' '))
        print(str("generala: %s    |" % self.print_points("generala")).rjust(25, ' '))
        print(str("double_generala: %s  |" % self.print_points("double_generala")).rjust(25, ' '))
        print(str("|").rjust(25, '-'))
        print(str("PUNTAJE: %s    |" % self.score).rjust(25, ' '))
        print(str("|").rjust(25, '-'))
