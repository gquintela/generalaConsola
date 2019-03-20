from generala.beaker import Beaker
from generala.rules import Rules
from generala.player import Player
from generala.prompts import Prompts

class Game:

    def __init__(self):
        self.rules = Rules()
        self.round= 1
        self.throw_number = 1
        self.players = []
        self.beaker = Beaker()
        self.prompts = Prompts()

    def add_player (self,player):
        new_player= Player()
        new_player.name = player
        self.players.append(new_player)