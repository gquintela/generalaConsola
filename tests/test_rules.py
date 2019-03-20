from unittest import TestCase, main
from generala.rules import Rules
from generala.game import Game
from generala.beaker import Beaker


class TestRules(TestCase):

    def test_number_count(self):
        rules = Rules()
        beaker = Beaker()
        for die in beaker.dice:
            die.value = 1
        self.assertEqual(rules.number_count(beaker, 1), 5)
        for die in range(5):
            beaker.dice[die].value = die + 1
        self.assertEqual(rules.number_count(beaker, die + 1), die + 1)

    def test_stairway(self):
        game = Game()
        game.beaker.custom_beaker(1, 2, 3, 4, 5)
        self.assertEqual(game.rules.compute_stairway(game, game.beaker), 25)
