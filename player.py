

class Player:
    def __init__(self):
        self.name= ""
        self.totalPoints=0
        self.throwNumber=0
        self.categories= {
            "UNO":(0,"empty"),
            "DOS":(0,"empty"),
            "TRES":(0,"empty"),
            "CUATRO":(0,"empty"),
            "CINCO":(0,"empty"),
            "SEIS":(0,"empty"),
            "ESCALERA":(0,"empty"),
            "FULL":(0,"empty"),
            "POKER":(0,"empty"),
            "GENERALA":(0,"empty"),
            "GENERALA DOBLE":(0,"empty")
        }