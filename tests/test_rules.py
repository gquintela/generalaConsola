from unittest import TestCase, main
from generala.judge import Judge
from generala.game import Game
from generala.beaker import Beaker


class TestRules(TestCase):

    def test_number_count(self):
        rules = Judge()
        game = Game()
        for die in game.beaker.dice:
            die.value = 1
        self.assertEqual(rules.number_count(game, 1), 5)
        for die in range(5):
            game.beaker.dice[die].value = die + 1
        self.assertEqual(rules.number_count(game, die + 1), die + 1)

    def test_stairway(self):
        game = Game()
        game.beaker.custom_beaker(1, 2, 3, 4, 5)
        self.assertEqual(game.judge.compute_stairway(game), 25)

    def test_poker(self):
        game = Game()
        game.beaker.custom_beaker(5,5,6,6,6)
        self.assertEqual(game.judge.compute_poker(game), 0)

if __name__ == '__main__':
    main()
